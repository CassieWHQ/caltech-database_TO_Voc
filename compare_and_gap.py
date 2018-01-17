import os

def get_xml_and_jpg_list(theFilePath):
    filenames = os.listdir(theFilePath)
    print 'len of filenames list is : ',len(filenames)
    xml_list = []
    jpg_list = []
    for file_name in filenames:
        if file_name.split('.')[-1] == 'xml':
            xml_list.append(file_name.split('.')[0])
        elif file_name.split('.')[-1] == 'jpg':
            jpg_list.append(file_name.split('.')[0])
    print 'the len of xml_file and jpg_file are : ',len(xml_list),'  ',len(jpg_list)
#    print xml_list[11],'  ',jpg_list[11]
    return xml_list,jpg_list

def delete_no_person_jpg(theFilePath):
    xml_list,jpg_list = get_xml_and_jpg_list(theFilePath)    
    toDelete_list = []
    for jpg_name in jpg_list:
        if jpg_name not in xml_list :
            toDelete_list.append(str(jpg_name+'.jpg'))
    print 'toDelete len is : ', len(toDelete_list)
    if len(toDelete_list) > 0 :
        for file_name in toDelete_list:
            os.remove(os.path.join(theFilePath,file_name))

def choose_by_gap(theFilePath,gap=3):
    xml_list,jpg_list = get_xml_and_jpg_list(theFilePath) 

    if not cmp(xml_list,jpg_list):
        print "the xml file != jpg file , break"
        return
    else:
        print "xml == jpg , continue..."
    xml_list.sort()
    #print xml_list   
    num_of_save = []
    #print 'dot'
    for _ in range(0,len(xml_list),gap):
        num_of_save.append(_)
    #print num_of_save  
    for i in range(0,len(xml_list)):
        #print i
        if i not in num_of_save:
            remove_path = os.path.join(theFilePath,xml_list[i])

            print 'the remove path is : ',remove_path

            os.remove(remove_path+'.xml')
            os.remove(remove_path+'.jpg')
    #print 'end'
    

if __name__ == '__main__':        
    theFilePath = 'set01V004'
    delete_no_person_jpg(theFilePath)
    choose_by_gap(theFilePath,5)
