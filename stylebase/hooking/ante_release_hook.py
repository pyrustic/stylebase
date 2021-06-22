# ante_release_hook.py generated by Pyrustic Manager
import os
import os.path
import sys
from jayson import Jayson


TEXT = """\
Released with [Pyrustic]({pyrustic_link}).
"""


def get_data():
    """
    Return None or a dict with the keys:
        'script', 'target', 'app_pkg' and 'version'
    """
    items = ("script", "target", "app_pkg", "version")
    data = None
    if len(sys.argv) == len(items):
        data = {item: sys.argv[i] for i, item in enumerate(items)}
    return data


def get_pyrustic_data_path(data):
    target = data["target"]
    app_pkg = data["app_pkg"]
    pyrustic_data_path = os.path.join(target, app_pkg,
                                      "pyrustic_data")
    if not os.path.exists(pyrustic_data_path):
        return None
    return pyrustic_data_path


def get_jayson(pyrustic_data_path, config_name, readonly):
    if not pyrustic_data_path:
        return None
    config_path = os.path.join(pyrustic_data_path,
                               config_name)
    if not os.path.exists(config_path):
        return None
    jayson = Jayson(config_path, readonly=readonly)
    return jayson


def get_release_description(target, owner, repo):
    latest_release_path = os.path.join(target, "LATEST_RELEASE.md")
    cache = None
    try:
        with open(latest_release_path, "r") as file:
            cache = file.read()
    except Exception as e:
        pass
    text = None
    if cache:
        text = cache
    else:
        text = _get_default_release_description(owner, repo)
    return text


def update_release_jayson(target,
                              release_jayson,
                              build_report_jayson,
                              app_pkg, version):
    text = "Missing data in $APP_DIR/pyrustic_data/{}"
    if not build_report_jayson.data:
        print(text.format("build_report.json"))
        return False
    if not release_jayson.data:
        print(text.format("release_info.json"))
        return False
    # update owner
    if not release_jayson.data["owner"]:
        owner = input("Github owner: ")
        print("")
        release_jayson.data["owner"] = owner
    # update repo
    if not release_jayson.data["repository"]:
        repo = os.path.basename(target)
        release_jayson.data["repository"] = repo
    # update name
    repo = release_jayson.data["repository"]
    name = "{} v{}".format(repo, version)
    release_jayson.data["release_name"] = name
    # update tag name
    tag_name = "v{}".format(version)
    release_jayson.data["tag_name"] = tag_name
    # update target commitish
    if not release_jayson.data["target_commitish"]:
        release_jayson.data["target_commitish"] = "master"
    # update description
    owner = release_jayson.data["owner"]
    repository = release_jayson.data["repository"]
    description = get_release_description(target, owner, repository)
    release_jayson.data["description"] = description
    # update is_prerelease
    if not release_jayson.data["is_prerelease"]:
        release_jayson.data["is_prerelease"] = False
    # update is_draft
    if not release_jayson.data["is_draft"]:
        release_jayson.data["is_draft"] = False
    # update upload_asset
    if release_jayson.data["upload_asset"] is None:
        release_jayson.data["upload_asset"] = True
    # update asset name
    asset_name = build_report_jayson.data["wheel_asset"]
    release_jayson.data["asset_name"] = asset_name
    # update asset label
    if not release_jayson.data["asset_label"]:
        release_jayson.data["asset_label"] = "Download the Wheel"
    # save the changes
    release_jayson.save()
    return True


def _get_default_release_description(owner, repo):
    pyrustic_link = "https://github.com/pyrustic/pyrustic"
    text = TEXT.format(pyrustic_link=pyrustic_link)
    return text


def main():
    data = get_data()
    if not data:
        print("Missing sys.argv data")
        sys.exit(1)
    pyrustic_data_path = get_pyrustic_data_path(data)
    # get build_report jayson
    build_report_jayson = get_jayson(pyrustic_data_path,
                                       "build_report.json", True)
    # get release info jayson
    release_jayson = get_jayson(pyrustic_data_path,
                                     "release_info.json", False)
    # update release_info.json
    if not update_release_jayson(data["target"],
                                     release_jayson,
                                     build_report_jayson,
                                     data["app_pkg"],
                                     data["version"]):
        sys.exit(1)
    # exit
    sys.exit(0)


if __name__ == "__main__":
    main()
