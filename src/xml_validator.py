import os
import xml.etree.ElementTree as ET

class XmlValidator:
    def __init__(self,address):
        self.address = address

    def check_xml_size(self , delete_empty = False):
        print("---> start checking xml size : ")
        count_mismatched = 0
        unsorted_xml_files = []


        for file in os.listdir(self.address):
            if file.endswith('.xml'):
                xml_path = os.path.join(self.address, file)
                if os.path.getsize(xml_path) == 0:
                    print(f"xml {xml_path} is empty")
                    unsorted_xml_files.append(xml_path)
                    if delete_empty == True:
                        os.remove(xml_path)
                    
        return count_mismatched, unsorted_xml_files

    def check_single_files(self):

        count_single = 0
        single_files = []


        for file in os.listdir(self.address):
            is_found = False
            if file.endswith(('.xml')):
                file_name, extension = os.path.splitext(file)
                image_extensions = [".jpg", ".jpeg", ".png"]

                for extension in image_extensions:
                    image_path = os.path.join(self.address, file_name + extension)

                    if os.path.isfile(image_path):
                        is_found = True
                        break

                if not is_found :
                    count_single += 1
                    single_files.append(file_name)

        print(f"we have {count_single} file that have no image or xml file")
        return count_single, single_files

    def check_format(self):
        print("---> start checking XML format:")
        unsorted_xml_files = []
        invalid_count = 0

        for file in os.listdir(self.address):
            if not file.endswith(".xml"):
                continue

            xml_path = os.path.join(self.address, file)

            # 1. Check XML syntax
            try:
                tree = ET.parse(xml_path)
                root = tree.getroot()
            except ET.ParseError:
                print(f"{file}: invalid XML syntax")
                invalid_count += 1
                unsorted_xml_files.append(file)
                continue

            errors = []

            # 2. Check root
            if root.tag != "annotation":
                errors.append("root tag must be <annotation>")

            # 3. Check filename
            filename = root.find("filename")

            if filename is None or not filename.text:
                errors.append("missing <filename>")

            # 4. Check image size
            size = root.find("size")

            width = None
            height = None

            if size is None:
                errors.append("missing <size>")
            else:
                width_tag = size.find("width")
                height_tag = size.find("height")
                depth_tag = size.find("depth")

                if width_tag is None or not width_tag.text:
                    errors.append("missing <width>")

                if height_tag is None or not height_tag.text:
                    errors.append("missing <height>")

                if depth_tag is None or not depth_tag.text:
                    errors.append("missing <depth>")

                try:
                    if width_tag is not None:
                        width = int(width_tag.text)

                    if height_tag is not None:
                        height = int(height_tag.text)

                except (TypeError, ValueError):
                    errors.append("width/height must be integers")

            # 5. Check objects
            objects = root.findall("object")

            if len(objects) == 0:
                errors.append("no <object> found")

            for index, obj in enumerate(objects, start=1):

                # Check class name
                name = obj.find("name")

                if name is None or not name.text:
                    errors.append(
                        f"object {index}: missing <name>"
                    )

                # Check bounding box
                bbox = obj.find("bndbox")

                if bbox is None:
                    errors.append(
                        f"object {index}: missing <bndbox>"
                    )
                    continue

                coordinates = {}

                for coordinate in ["xmin", "ymin", "xmax", "ymax"]:
                    tag = bbox.find(coordinate)

                    if tag is None or not tag.text:
                        errors.append(
                            f"object {index}: missing <{coordinate}>"
                        )
                        continue

                    try:
                        coordinates[coordinate] = int(tag.text)
                    except ValueError:
                        errors.append(
                            f"object {index}: {coordinate} must be integer"
                        )

                # Cannot validate bbox if some coordinates are missing
                if len(coordinates) != 4:
                    continue

                xmin = coordinates["xmin"]
                ymin = coordinates["ymin"]
                xmax = coordinates["xmax"]
                ymax = coordinates["ymax"]

                # Check bbox geometry
                if xmin >= xmax:
                    errors.append(
                        f"object {index}: xmin must be smaller than xmax"
                    )

                if ymin >= ymax:
                    errors.append(
                        f"object {index}: ymin must be smaller than ymax"
                    )

                # Check negative coordinates
                if xmin < 0 or ymin < 0:
                    errors.append(
                        f"object {index}: bbox contains negative coordinates"
                    )

                # Check bbox against image size
                if width is not None and xmax > width:
                    errors.append(
                        f"object {index}: xmax ({xmax}) exceeds image width ({width})"
                    )

                if height is not None and ymax > height:
                    errors.append(
                        f"object {index}: ymax ({ymax}) exceeds image height ({height})"
                    )

            # Final result for this XML
            if errors:
                invalid_count += 1

                print(f"\n{file} is INVALID:")

                for error in errors:
                    print(f"  - {error}")

            else:
                print(f"{file}: OK")

        print(f"\nInvalid XML files: {invalid_count}")

        return invalid_count, unsorted_xml_files
                    


    def xml_validation(self,delete_empty = False , check_format = False , output_file = None):
        f1 = open(output_file, "a")
        f1.write(f"\nxml validation started for {self.address} \n")
        invalid_count, unsorted_xml_files = self.check_xml_size(delete_empty=delete_empty)
        f1.write(f"we have {invalid_count} invalid XML files\n")
        for file in unsorted_xml_files:
            f1.write(f"invalid file: {file}\n")
        count_single, single_files = self.check_single_files()
        f1.write(f"we have {count_single} files that have no image or xml file\n")
        for file_name in single_files:
            f1.write(f"single file: {file_name}\n")
        if check_format:
            invalid_count_format, unsorted_xml_files_format = self.check_format()
            f1.write(f"we have {invalid_count_format} XML files with format issues\n")
            for file in unsorted_xml_files_format:
                f1.write(f"format issue file: {file}\n")
        f1.close()
