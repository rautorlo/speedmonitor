
# ========================================
# ADD TO MAIN LOG
# ========================================
# This function add the last values to
# stored in @param current_file_log to the 
# @param general_file_log

def word_in_file_replace(current_file_log, general_file_log):

    source_file = open(source_file_name,"r+")
    new_file = []


    for line in source_file:
        if word_i in line:
            line = line.replace(word_i, word_o)
        new_file.append(line)

    source_file.close()
    source_file = open(source_file_name,"w+")
    source_file.writelines(new_file)
    source_file.close()
    return;