import os
import in_place
osPath = r"C:\Users\Pre-Installed User\Documents\adapters_try"
bd_version = "Bundle-Version"


def find_manifest(name, path):
    list_of_manifest = []
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if name in dir:
                manifest_dir = os.path.join(root, dir, 'MANIFEST.MF')
                manifest_dir = manifest_dir.replace('\\', '/')
                list_of_manifest.append(manifest_dir)
    return list_of_manifest


def increment_version(bundle_version):
    plugin_version = bundle_version.replace('\n', '').replace(' ', '').split(":")[1]
    id = plugin_version.split('.')
    n = len(id)
    while n > 0:
        last_id = int(id[n-1]) + 1
        if last_id > 9:
            id[n - 1] = '0'
            n -= 1
        else:
            id[n - 1] = str(last_id)
            break
    final_id = '.'.join(id) + '\n'
    final_line = bd_version + ": " + final_id
    # print(final_line)
    # print(bundle_version)
    return final_line


def modify_plugin_id(manifests):
    for mf in manifests:
        with in_place.InPlace(mf) as fp:
            for line in fp:
                if bd_version in line:
                    # let go of qualifer
                    line = line.replace('.qualifier', '')
                    # increment version
                    line = increment_version(line)
                    # print(line)
                fp.write(line)


if __name__ == '__main__':
    # first: search for all plugins in the bundle
    listOfManifest = find_manifest('META-INF', osPath)
    print(listOfManifest)
    # second: read the file
    # file1 = listOfManifest[0]
    # print(os.path.exists(file1))
    modify_plugin_id(listOfManifest)

