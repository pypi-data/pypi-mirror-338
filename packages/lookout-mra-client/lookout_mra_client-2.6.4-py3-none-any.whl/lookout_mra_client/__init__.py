import build.util, os


def __get_version():
    this_dir = os.path.dirname(__file__)
    project_dir = os.path.join(this_dir, "..", "..")
    project_metadata = build.util.project_wheel_metadata(project_dir)

    return project_metadata.get("version")


__version__ = __get_version()
__prj_name__ = f"lookout-mra-client/{__version__}"
