import os
import in_place
import argparse
from lxml import etree


class RcpVersionManager:
    my_dict = {'META-INF' : 'META-INF/MANIFEST.MF', '.feature' : 'feature.xml'}
    bd_version = "Bundle-Version"

    def __init__(self, args):
        self._args = args
        self._path = args.path.replace('\\', '/')
        # self._bundle_loc = self._path + '/bundles'
        # self._feature_loc = self._path + '/features'
        # self._product_loc = self._path + '/products'

    def find_file_loc(self, name_of_dir, what_to_search):
        list_of_file = []
        path_to_search = self._path + '/' + name_of_dir
        subdir = os.listdir(path_to_search)
        for directoryName in subdir:
            manifest_dir = os.path.join(path_to_search, directoryName, self.my_dict.get(what_to_search))
            manifest_dir = manifest_dir.replace('\\', '/')
            if os.path.exists(manifest_dir):
                list_of_file.append(manifest_dir)
        return list_of_file

    def modify_plugin_id(self, manifests):
        for mf in manifests:
            with in_place.InPlace(mf) as fp:
                for line in fp:
                    if self.bd_version in line and '.qualifier' in line:
                        # let go of qualifer
                        line = line.replace('.qualifier', '')
                        # increment version
                        line = self.increment_version(line)
                        # print(line)
                    fp.write(line)

    def increment_version(self, bundle_version):
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
        final_line = self.bd_version + ": " + final_id
        # print(final_line)
        # print(bundle_version)
        return final_line

    def modify_dpd(self, loc):
        # 1. update about.mappings
        # self.modify_dpd_about_mappings(loc)
        # 2. update plugin.xml with (add another tag for release date)
        self.modify_dpd_plugin_xml(loc)

    def modify_feature(self):
        path = self._path + '/features'
        list_of_feature = self.find_file_loc('features', '.feature')
        for feature_file in list_of_feature:
            print('tes')

    def modify_dpd_about_mappings(self, loc):
        location = self._path + '/' + loc + '/about.mappings'
        with in_place.InPlace(location) as fp:
            for line in fp:
                if '-SNAPSHOT' in line:
                    # let go of qualifer
                    line = line.replace('-SNAPSHOT', '.0000')
                    # print(line)
                fp.write(line)
        # TODO: Need to add date to about.mappings

    def modify_dpd_plugin_xml(self, loc):
        # https://docs.python.org/2/library/xml.etree.elementtree.html
        location = self._path + '/' + loc + '/plugin.xml'
        et = etree.parse(location)
        tag1 = et.getroot()
        for child in tag1:
            print(child.tag, child.attrib)
        for extension in tag1.findall('extension'):
            if extension.get('point') == 'org.eclipse.core.runtime.adapters':
                target_ext = extension
                break
        factory_node = target_ext.find('factory')
        print(factory_node.get('class'))
        new_tag = etree.SubElement(factory_node, 'adapter')
        new_tag.attrib['type'] = 'banana'
        et.write(location, xml_declaration=True, pretty_print=True, encoding='UTF-8')


    def execute(self):
        # now the path location is C:/ST/DPDMC for e.g.
        # step 1: make changes to release note in com.gemalto.dpd (about.mappings & plugin.xml) if necessary:
        if self._args.release:
            self.modify_dpd('org.eclipse.articles.adapters.properties')

        # step 2: increment all plugin id. (including that of com.gemalto.dpd)
        # list_of_manifest = self.find_file_loc('bundles', 'META-INF')
        # self.modify_plugin_id(list_of_manifest)

        # step 3: Update feature version
        # self.modify_feature()
        # if self._args.feature:
        #     self.modify_feature()


def main():
    parser = argparse.ArgumentParser(description='this is a program that increment plugin ids')
    parser.add_argument('path', help="location of DPDMC/DPDCore folder")
    parser.add_argument('-r', '--release', action='store_true', default=False)
    parser.add_argument("-f", "--feature", action='store_true', default=False)
    rcp_manager = RcpVersionManager(parser.parse_args([r'C:\Users\Pre-Installed User\Documents\adapters_try', '-r']))
    # rcp_manager = RcpVersionManager(parser.parse_args())
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

