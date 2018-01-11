# Deal with .seq format for video sequence
# Author: Kaij
# The .seq file is combined with images,
# so I split the file into several images with the image prefix
# "\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46".

import os.path
import fnmatch
import shutil


def open_save(file, savepath, setname, seqfilename):
    # read .seq file, and save the images into the savepath

    f = open(file, 'rb')
    string = str(f.read())
    splitstring = "\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46"
    # split .seq file into segment with the image prefix
    strlist = string.split(splitstring)
    f.close()
    count = 0
    # delete the image folder path if it exists
    # if os.path.exists(savepath):
    #     shutil.rmtree(savepath)
    # create the image folder path
    # if not os.path.exists(savepath):
    #     os.makedirs(savepath)
    # deal with file segment, every segment is an image except the first one
    for img in strlist:
        filename = 'cal_' + setname + '_' + seqfilename.split('.')[0] + '_' + 'I' + str(count).zfill(5) + '.jpg'
        filenamewithpath = os.path.join(savepath, filename)
        # abandon the first one, which is filled with .seq header
        if count > 0:
            i = open(filenamewithpath, 'wb+')
            i.write(splitstring)
            i.write(img)
            i.close()
        count += 1


#if __name__=="__main__":

def seq2jpg_main(rootdir,out_dir):
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print 'start  seq2jpg processing..'
    #rootdir = 'data/seq_file/set00/set00'
    #out_dir = 'data/images/set00V001'
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
    
    # walk in the rootdir, take down the .seq filename and filepath
    # print 'OK'
    for parent, dirnames, filenames in os.walk(rootdir):
        #
        # print 'parent :',(parent)
        # print 'dirnames :' , (dirnames)
        # print 'filename:', (filenames)

        if dirnames ==[]:
            setname = parent.split('/')[-1]
            for filename in filenames:
                # check .seq file with suffix
                if fnmatch.fnmatch(filename,'*.seq'):
                    # take down the filename with path of .seq file
                    # thefilename = os.path.join(parent, filename)
                    thefilename = os.path.join(parent, filename)
                    # create the image folder by combining .seq file path with .seq filename
                    # thesavepath = parent+'/'+filename.split('.')[0]
                    thesavepath = os.path.join(out_dir,setname,filename.split('.')[0])
                    print "Filename=" + thefilename
                    print "Savepath=" + thesavepath
                    if not os.path.exists(thesavepath):
                        os.makedirs(thesavepath)
                    open_save(thefilename,thesavepath,setname,filename)
    print 'end  seq2jpg processing..'
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
