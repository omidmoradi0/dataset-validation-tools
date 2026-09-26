import os 
import cv2

class XmlValidator:
    def __init__(self,address):
        self.address = address

    def check_xml_size(self , delete_empty = False):
        print("---> start checking xml size : ")
        count_mismatched = 0

        for file in os.listdir(self.address):
            if file.endswith('.xml'):
                xml_path = os.path.join(self.address, file)
                if os.path.getsize(xml_path) == 0:
                    print(f"xml {xml_path} is empty")
                    if delete_empty == True:
                        os.remove(xml_path)
                    
        return count_mismatched 

    def check_single_files(self):

        count_single = 0


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

        print(f"we have {count_single} file that have no image or xml file")

    def xml_validation(self,delete_empty = False):
        self.check_xml_size(delete_empty=delete_empty)
        self.check_single_files()
