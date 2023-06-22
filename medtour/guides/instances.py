import os


def get_program_path(instance, filename):
    return os.path.join('programs', "program_%s" % str(instance.id), filename)


def get_shots_path(instance, filename):
    return os.path.join('guide_shots', "guide_%s" % str(instance.program.id), filename)


def get_program_shots_path(instance, filename):
    return os.path.join('program_shots', "program_%s" % str(instance.program.id), filename)
