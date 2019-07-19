import os
import in_place
import argparse
osPath = r"C:\Users\Pre-Installed User\Documents\adapters_try"
bd_version = "Bundle-Version"


class RcpPluginManager:
    name = 'META-INF'

    def __init__(self, args):
        self._args = args

    def find_manifest(self, path):
        list_of_manifest = []
        for root, dirs, files in os.walk(path):
            for directoryName in dirs:
                if self.name in directoryName:
                    manifest_dir = os.path.join(root, directoryName, 'MANIFEST.MF')
                    manifest_dir = manifest_dir.replace('\\', '/')
                    list_of_manifest.append(manifest_dir)
        return list_of_manifest

    def modify_plugin_id(self, manifests):
        for mf in manifests:
            with in_place.InPlace(mf) as fp:
                for line in fp:
                    if bd_version in line:
                        # let go of qualifer
                        line = line.replace('.qualifier', '')
                        # increment version
                        line = self.increment_version(line)
                        # print(line)
                    fp.write(line)

    @staticmethod
    def increment_version(bundle_version):
        plugin_version = bundle_version.replace('\n', '').replace(' ', '').split(":")[1]
        plugin_id = plugin_version.split('.')
        n = len(plugin_id)
        while n > 0:
            last_id = int(plugin_id[n - 1]) + 1
            if last_id > 9:
                plugin_id[n - 1] = '0'
                n -= 1
            else:
                plugin_id[n - 1] = str(last_id)
                break
        final_id = '.'.join(plugin_id) + '\n'
        final_line = bd_version + ": " + final_id
        # print(final_line)
        # print(bundle_version)
        return final_line

    def execute(self):
        list_of_manifest = self.find_manifest(self._args.path)
        self.modify_plugin_id(list_of_manifest)


def main():
    parser = argparse.ArgumentParser(description='this is a program that increment plugin ids')
    parser.add_argument('path', help="location of DPDMC folder")
    parser.add_argument("-f", "--feature", action='store_true', default=False)
    print(parser.parse_args().feature)
    rcp_manager = RcpPluginManager(parser.parse_args())
    rcp_manager.execute()


if __name__ == '__main__':
    main()
    # first: search for all plugins in the bundle
    # listOfManifest = find_manifest('META-INF', osPath)
    # print(listOfManifest)
    # # second: read the file
    # # file1 = listOfManifest[0]
    # # print(os.path.exists(file1))
    # modify_plugin_id(listOfManifest)

