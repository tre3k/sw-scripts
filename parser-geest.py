#!/usr/bin/env python3
# just script for simple convret from HZG fromato to my format


import xml.etree.ElementTree as ET
import os
import sys
import glob

src_dir = "../FeNi_Nov06"
work_dir = "./converted_maps"

src_files = glob.glob(src_dir+"/*.xml")

field_list = []
data_matrixs_up = dict()
data_matrixs_down = dict()


matrix_size = 256 #pix
pixel_resolution = 2.2 # mm
wavelenght = 5.7 # angstrom 
source_detector = 6.5 #m
temperature = 300 #K


for path_file in src_files:
    input_file = os.path.split(path_file)[-1]
    field_text = input_file.split('_')[2]
    pol_text = input_file.split('_')[3]
    num_text = input_file.split('_')[4]
    
    volts = field_text.replace('h','')
    volts = volts.replace('v','')
    volts = int(volts)

    issue_field = 0.0165*volts
    if volts == 17:
        issue_field = 0.230
    if volts == 20:
        issue_field = 0.312
    if volts == 25:
        issue_field = 0.320
        
    
    add_field = True
    for field in field_list:
        if field == field_text:
            add_field = False

    if add_field:
        field_list.append(field_text)

    xml_tree = ET.parse(path_file)
    xml_root = xml_tree.getroot()


    for xml_child in xml_root:
        #print(xml_child.tag, xml_child.attrib)
        for xml_sub_child in xml_child:
            #print(xml_sub_child.tag, xml_sub_child.attrib)

            if xml_sub_child.tag == 'counter' and  xml_sub_child.attrib['id'] == '6502mc_0x80-1':
                for xml_subsub_child in xml_sub_child:
                    if xml_subsub_child.tag=='value':
                        monitor1_value = xml_subsub_child.text

            if xml_sub_child.tag == 'counter' and  xml_sub_child.attrib['id'] == '6502mc_0x80-2':
                for xml_subsub_child in xml_sub_child:
                    if xml_subsub_child.tag=='value':
                        monitor2_value = xml_subsub_child.text

            if xml_sub_child.tag == 'counter' and  xml_sub_child.attrib['id'] == '6502mc_0x80-3':
                for xml_subsub_child in xml_sub_child:
                    if xml_subsub_child.tag=='value':
                        monitor3_value = xml_subsub_child.text

            if xml_sub_child.tag == 'time' and  xml_sub_child.attrib['id'] == 'MCA' and xml_sub_child.attrib['name'] == 'rt':
                for xml_subsub_child in xml_sub_child:
                    if xml_subsub_child.tag=='value':
                        realtime = float(xml_subsub_child.text)


            if xml_sub_child.tag=='spectrum' and xml_sub_child.attrib['id']=='MCA':
                for xml_subsub_child in xml_sub_child:
                    if xml_subsub_child.tag=='resolution':
                        resolution = xml_subsub_child.text
                    if xml_subsub_child.tag=='value':
                        matrix_value = xml_subsub_child.text
                        
            

#    print(monitor3_value,monitor2_value,monitor1_value)
#    print(int(monitor1_value)/int(monitor2_value))

#    print(input_file)

    matrix = []
    for matrix_el in matrix_value.split():
        matrix.append(int(matrix_el))

# Write    

    fd = open(work_dir+"/"+field_text+"_"+pol_text+"_"+num_text+".mxm",'w')

    header = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    header = header + "<!DOCTYPE gelimagnetprocessing>\n<emulatedFormat>\n\t<filds>\n"
    header = header + "\t\t<Init>"+str(matrix_size)+"</Init>\n"
    header = header + "\t\t<MagneticFild>"+str(issue_field)+"</MagneticFild>\n"
    header = header + "\t\t<TimeOfExposition>"+str(realtime)+"</TimeOfExposition>\n"
    header = header + "\t\t<ResolutionOfDetector>"+str(pixel_resolution)+"</ResolutionOfDetector>\n"
    header = header + "\t\t<DistDetectorSource>"+str(source_detector)+"</DistDetectorSource>\n"
    header = header + "\t\t<Monitor1>"+str(monitor1_value)+"</Monitor1>\n"
    header = header + "\t\t<Lambda>"+str(wavelenght)+"</Lambda>\n"
    header = header + "\t\t<Temperature>"+str(temperature)+"</Temperature>\n"

    
    end = "\t</filds>\n</emulatedFormat>\n"
    
    fd.write(header)    

    fd.write("\t\t<Data>")
    for m_el in matrix:
        fd.write(str(m_el)+";")
        
    fd.write("<Data>\n")
    fd.write(end)
    
    


