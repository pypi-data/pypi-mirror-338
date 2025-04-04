# -*- coding: utf-8 -*-
# Copyright (c) 2020-2024 Salvador E. Tropea
# Copyright (c) 2020-2024 Instituto Nacional de Tecnologïa Industrial
# Copyright (c) 2019 Jesse Vincent (@obra)
# Copyright (c) 2018-2019 Seppe Stas (@seppestas) (Productize SPRL)
# Based on ideas by: Scott Bezek (@scottbez1)
# License: Apache 2.0
# Project: KiAuto (formerly kicad-automation-scripts)
# Adapted from: https://github.com/obra/kicad-automation-scripts
"""
Utilities related to the filesystem and file names.

Note: Only wait_for_file_created_by_process is from the original project.
"""
import os
import time
import re
import shlex
import shutil
import atexit
import subprocess
# python3-psutil
import psutil
import json

from kiauto.misc import WRONG_ARGUMENTS, KICAD_VERSION_5_99, Config, READ_ONLY_PROBLEM, RULES_KEY, KICAD_CLI_ERROR
from kiauto import log
logger = log.get_logger(__name__)
time_out_scale = 1.0


def set_time_out_scale(scale):
    global time_out_scale
    time_out_scale = scale


def wait_for_file_created_by_process(pid, file):
    global time_out_scale
    timeout = 15*time_out_scale
    process = psutil.Process(pid)
    DELAY = 0.2
    for j in range(2):
        # 2 passes: 1) for the file to be created 2) extend the timeout if created
        logger.debug('Waiting for file %s (pid %d) (timeout: %f)', file, pid, timeout)
        for i in range(int(timeout/DELAY)):
            kicad_died = False
            try:
                open_files = process.open_files()
            except psutil.AccessDenied:
                # Is our child, this access denied is because we are listing
                # files for other process that took the pid of the old KiCad.
                kicad_died = True
            if kicad_died:
                raise RuntimeError('KiCad unexpectedly died')
            logger.debug(open_files)
            if os.path.isfile(file):
                file_open = False
                for open_file in open_files:
                    if open_file.path == file:
                        file_open = True
                if file_open:
                    logger.debug('Waiting for process to close file')
                else:
                    return
            else:
                logger.debug('Waiting for process to create file')
            time.sleep(DELAY)
        # If the file was created assume KiCad is working
        if os.path.isfile(file):
            timeout = 45*time_out_scale
        else:
            # The file wasn't even created, don't wait much
            timeout = 1*time_out_scale

    raise RuntimeError('Timed out waiting for creation of %s' % file)


def load_filters(cfg, file):
    """ Load errors filters """
    if not os.path.isfile(file):
        logger.error("Filter file `{}` doesn't exist".format(file))
        exit(WRONG_ARGUMENTS)
    logger.debug('Loading filter errors')
    with open(file, 'r') as f:
        ln = 1
        fl = 0
        for line in f:
            line = line.rstrip()
            if len(line) > 0 and line[0] != '#':
                m = re.search(r'^(\S+)\s*,(.*)$', line)
                if m:
                    cfg.err_filters.append([m.group(1), m.group(2)])
                    fl = fl+1
                else:
                    logger.error('Syntax error at line {} in filter file `{}`: `{}`'.format(ln, file, line))
                    logger.error('Use `ERROR_NUMBER,REGEX` format')
                    exit(WRONG_ARGUMENTS)
            ln = ln+1
        logger.info('Loaded {} error filters from `{}`'.format(fl, file))


def add_filter(cfg, id, regex):
    cfg.err_filters.append((id, regex))


def apply_filters(cfg, err_name, wrn_name):
    """ Apply the error filters to the list of errors and unconnecteds """
    if len(cfg.err_filters) == 0:
        return (0, 0)
    skip_err = 0
    for i, err in enumerate(cfg.errs):
        for f in cfg.err_filters:
            if err.startswith('({})'.format(f[0])):
                m = re.search(f[1], err)
                if m:
                    skip_err += 1
                    logger.warning('Ignoring '+err)
                    logger.debug('Matched regex `{}`'.format(f[1]))
                    cfg.errs[i] = None
                    break
    if skip_err:
        logger.info('Ignoring {} {}'.format(skip_err, err_name))
    skip_wrn = 0
    for i, wrn in enumerate(cfg.wrns):
        for f in cfg.err_filters:
            if wrn.startswith('({})'.format(f[0])):
                m = re.search(f[1], wrn)
                if m:
                    skip_wrn += 1
                    logger.info('Ignoring '+wrn)
                    logger.debug('Matched regex `{}`'.format(f[1]))
                    cfg.wrns[i] = None
                    break
    if skip_wrn:
        logger.info('Ignoring {} {}'.format(skip_wrn, wrn_name))
    return skip_err, skip_wrn


def list_errors(cfg):
    for err in cfg.errs:
        if err:
            if "; Severity: warning" in err:
                logger.warning(re.sub(" +; Severity: warning\n?", '', err))
            else:
                logger.error(re.sub(" +; Severity: error\n?", '', err))


def list_warnings(cfg):
    for wrn in cfg.wrns:
        if wrn:
            if "; Severity: error" in wrn:
                logger.error(re.sub(" +; Severity: error\n?", ''), wrn)
            else:
                logger.warning(re.sub(" +; Severity: warning\n?", '', wrn))


def check_kicad_config_dir(cfg):
    if not os.path.isdir(cfg.kicad_conf_path):
        logger.debug('Creating KiCad config dir')
        os.makedirs(cfg.kicad_conf_path, exist_ok=True)


def remove_lib_table(fname):
    if os.path.isfile(fname):
        logger.debug('Removing '+fname)
        os.remove(fname)


def check_lib_table(fuser, fsys):
    if not os.path.isfile(fuser):
        logger.debug('Missing default '+os.path.basename(fuser))
        for f in fsys:
            if os.path.isfile(f):
                shutil.copy2(f, fuser)
                logger.debug('Copied {} to {}'.format(f, fuser))
                return
        logger.warning('Missing default system symbol table '+fsys[0] +
                       ' creating an empty one')  # pragma: no cover
        with open(fuser, 'wt') as f:
            f.write('({} )\n'.format(os.path.basename(fuser).replace('-', '_')))
        atexit.register(remove_lib_table, fuser)


def restore_one_config(name, fname, fbkp):
    if fbkp and os.path.exists(fbkp):
        if os.path.exists(fname):
            os.remove(fname)
        os.rename(fbkp, fname)
        logger.debug('Restoring old %s config', name)
        return None
    return fbkp


def restore_config(cfg):
    """ Restore original user configuration """
    cfg.conf_eeschema_bkp = restore_one_config('eeschema', cfg.conf_eeschema, cfg.conf_eeschema_bkp)
    cfg.conf_kicad_bkp = restore_one_config('KiCad common', cfg.conf_kicad, cfg.conf_kicad_bkp)
    cfg.conf_hotkeys_bkp = restore_one_config('user hotkeys', cfg.conf_hotkeys, cfg.conf_hotkeys_bkp)
    cfg.conf_pcbnew_bkp = restore_one_config('pcbnew', cfg.conf_pcbnew, cfg.conf_pcbnew_bkp)
    cfg.conf_colors_bkp = restore_one_config('colors', cfg.conf_colors, cfg.conf_colors_bkp)
    cfg.conf_3dview_bkp = restore_one_config('3D viewer', cfg.conf_3dview, cfg.conf_3dview_bkp)


def backup_config(name, file, err, cfg):
    config_file = file
    old_config_file = file+'.pre_script'
    logger.debug(name+' config: '+config_file)
    # If we have an old back-up ask for the user to solve it
    if os.path.isfile(old_config_file):
        logger.error(name+' config back-up found (%s)', old_config_file)
        logger.error('It could contain your %s configuration, rename it to %s or discard it.', name.lower(), config_file)
        exit(err)
    if os.path.isfile(config_file):
        logger.debug('Moving current config to '+old_config_file)
        os.rename(config_file, old_config_file)
        atexit.register(restore_config, cfg)
        return old_config_file
    return None


def create_user_hotkeys(cfg):
    logger.debug('Creating a user hotkeys config')
    with open(cfg.conf_hotkeys, "wt") as text_file:
        text_file.write('common.Control.print\tCtrl+P\n')
        text_file.write('common.Control.plot\tCtrl+Shift+P\n')
        text_file.write('common.Control.show3DViewer\tAlt+3\n')
        text_file.write('eeschema.EditorControl.exportNetlist\tCtrl+Shift+N\n')
        text_file.write('eeschema.EditorControl.generateBOM\tCtrl+Shift+B\n')
        text_file.write('eeschema.InspectionTool.runERC\t{}\n'.format(RULES_KEY))
        text_file.write('pcbnew.DRCTool.runDRC\t{}\n'.format(RULES_KEY))
        text_file.write('pcbnew.ZoneFiller.zoneFillAll\tB\n')
        text_file.write('pcbnew.EditorControl.generateD356File\tAlt+Shift+E\n')
        text_file.write('3DViewer.Control.rotateXclockwise\tAlt+X\n')
        text_file.write('3DViewer.Control.rotateXcounterclockwise\tAlt+Shift+X\n')
        text_file.write('3DViewer.Control.rotateYclockwise\tAlt+Y\n')
        text_file.write('3DViewer.Control.rotateYcounterclockwise\tAlt+Shift+Y\n')
        text_file.write('3DViewer.Control.rotateZclockwise\tAlt+Z\n')
        text_file.write('3DViewer.Control.rotateZcounterclockwise\tAlt+Shift+Z\n')


def create_kicad_config(cfg):
    logger.debug('Creating a KiCad common config')
    with open(cfg.conf_kicad, "wt") as text_file:
        if cfg.conf_kicad_json:
            kiconf = {"environment": {"show_warning_dialog": False}}
            kiconf['graphics'] = {"cairo_antialiasing_mode": 0, "opengl_antialiasing_mode": 0}
            kiconf['system'] = {"editor_name": "/bin/cat"}
            # Copy the environment vars if available
            if cfg.conf_kicad_bkp:
                vars = Config.get_config_vars_json(cfg.conf_kicad_bkp, logger)
                if vars:
                    kiconf['environment']['vars'] = vars
            text_file.write(json.dumps(kiconf))
            logger.debug(json.dumps(kiconf))
        else:
            text_file.write('ShowEnvVarWarningDialog=0\n')
            text_file.write('Editor=/bin/cat\n')
            # Copy the environment vars if available
            if cfg.conf_kicad_bkp:
                vars = Config.get_config_vars_ini(cfg.conf_kicad_bkp)
                if vars:
                    text_file.write('[EnvironmentVariables]\n')
                    for key in vars:
                        text_file.write(key.upper()+'='+vars[key]+'\n')


def restore_autosave(name):
    """ Restores de auto save information """
    old_name = name[:-11]
    if os.path.isfile(name):
        logger.debug('Restoring {} -> {}'.format(name, old_name))
        os.rename(name, old_name)


def check_input_file(cfg, no_file, no_ext):
    # Check the schematic/PCB is there
    if not os.path.isfile(cfg.input_file):
        logger.error(cfg.input_file+' does not exist')
        exit(no_file)
    # If we pass a name without extension KiCad will try to create a kicad_sch/kicad_pcb
    # The extension can be anything.
    ext = os.path.splitext(cfg.input_file)[1]
    if not ext:
        logger.error('Input files must use an extension, otherwise KiCad will reject them.')
        exit(no_ext)
    if cfg.kicad_version >= KICAD_VERSION_5_99 and ext == '.sch':
        logger.warning('Using old format files is not recommended. Convert them first.')
    # KiCad 6 uses #auto_saved_files# to store autosave info
    fauto = os.path.join(os.path.dirname(cfg.input_file), '#auto_saved_files#')
    if os.path.isfile(fauto):
        logger.warning('Partially saved project detected, please double check it')
        # Rename it so KiCad doesn't ask about restoring autosaved files
        fauto_new = fauto+'.moved_away'
        logger.debug('Renaming {} -> {}'.format(fauto, fauto_new))
        try:
            os.rename(fauto, fauto_new)
        except PermissionError:
            # Read-only directory or file system, give up
            logger.error('Unable to rename `{}` please remove it manually'.format(fauto))
            exit(READ_ONLY_PROBLEM)
        # Restore it at exit
        atexit.register(restore_autosave, fauto_new)


def memorize_project(cfg):
    """ Detect the .pro filename and try to read it and its mtime.
        If KiCad changes it then we'll try to revert the changes """
    cfg.pro_stat = None
    cfg.pro_content = None
    cfg.prl_stat = None
    cfg.prl_content = None
    name_no_ext = os.path.splitext(cfg.input_file)[0]
    cfg.pro_name = name_no_ext+'.'+cfg.pro_ext
    if not os.path.isfile(cfg.pro_name):
        cfg.pro_name = name_no_ext+'.pro'
        if not os.path.isfile(cfg.pro_name):
            logger.warning('KiCad project file not found')
            cfg.pro_name = name_no_ext+'.'+cfg.pro_ext
            return
        if cfg.kicad_version >= KICAD_VERSION_5_99:
            logger.warning('Using old format projects is not recommended. Convert them first.')
    if cfg.pro_name[-4:] == '.pro':
        cfg.pro_stat = cfg.start_pro_stat
    else:
        cfg.pro_stat = cfg.start_kicad_pro_stat
    with open(cfg.pro_name, 'rb') as f:
        cfg.pro_content = f.read()
    atexit.register(restore_project, cfg)
    if cfg.prl_ext:
        cfg.prl_name = name_no_ext+'.'+cfg.prl_ext
        if not os.path.isfile(cfg.prl_name):
            return
        cfg.prl_stat = cfg.start_kicad_prl_stat
        with open(cfg.prl_name, 'rb') as f:
            cfg.prl_content = f.read()


def _restore_project(name, stat_v, content):
    logger.debug('Checking if %s was modified', name)
    if stat_v and content:
        pro_found = False
        if os.path.isfile(name):
            new_stat = os.stat(name)
            pro_found = True
        else:  # pragma: no cover
            logger.warning('Project file lost')
        if not pro_found or new_stat.st_mtime != stat_v.st_mtime:
            logger.debug('Restoring the project file')
            os.rename(name, name+'-bak')
            with open(name, 'wb') as f:
                f.write(content)
            os.utime(name, times=(stat_v.st_atime, stat_v.st_mtime))


def restore_project(cfg):
    """ If the .pro was modified try to restore it """
    _restore_project(cfg.pro_name, cfg.pro_stat, cfg.pro_content)
    if cfg.prl_ext and cfg.prl_stat:
        _restore_project(cfg.prl_name, cfg.prl_stat, cfg.prl_content)


def get_log_files(out_dir, app_name, also_interposer=False):
    if log.get_level() > 2:
        os.makedirs(out_dir, exist_ok=True)
        flog_out = open(os.path.join(out_dir, app_name+'_out.log'), 'wt')
        flog_err = open(os.path.join(out_dir, app_name+'_err.log'), 'wt')
        logger.debug('Redirecting '+app_name+' output to '+app_name+'*.log')
    else:
        flog_out = flog_err = subprocess.DEVNULL
    if also_interposer:
        os.makedirs(out_dir, exist_ok=True)
        fname = os.path.join(out_dir, app_name+'_interposer.log')
        flog_int = open(fname, 'wt')
        logger.debug('Saving '+app_name+' interposer dialog to '+fname)
    else:
        flog_int = subprocess.DEVNULL
    return (flog_out, flog_err, flog_int)


def debug_output(res):
    if res.stdout:
        logger.debug('- Output from command: '+res.stdout.decode())


def run_command(command, check=True):
    logger.debug('Executing: '+shlex.join(command))
    try:
        res = subprocess.run(command, check=check, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        logger.error('Running {} returned {}'.format(e.cmd, e.returncode))
        debug_output(e)
        exit(KICAD_CLI_ERROR)
    debug_output(res)
    return res.stdout.decode().rstrip()
