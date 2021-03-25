import json
import os, re

#Function to count all messages per chat
def count_messages(filepath):
    name = "Group"
    group = False
    count = 0
    
    with open(filepath, "r") as f:
        messages = json.load(f)
        if len(messages["participants"]) > 2:
            group = True
        else:
            name = messages["participants"][0]["name"]
        count = len(messages["messages"])
        
    return (name, count, group)

#Input your path here
#path = "./facebook-evgheniiberiozchin/messages/inbox"

def count_from_path(path):
    #Count by chat
    counts = []

    for folder in os.listdir(path):
        count = 0
        for file in os.listdir(path + "/" + folder):
            if re.match(r"message_[0-9]+.json", file):
                (name, file_count, group) = count_messages(path + "/" + folder + "/" + file)
                count += file_count
        if group:
            name = folder[:folder.find("_")]
        counts.append((name, count, group))

    #Top 30 private chats by nr. of messages       
    private_chats_counts = filter(lambda count_tuple : not count_tuple[2], counts)
    private_chats_counts = sorted(private_chats_counts, key = lambda count_tuple : count_tuple[1], reverse = True)
    output_list1 = []
    
    for count_tuple in private_chats_counts[:10]:
        output_list1.append("{}: {}".format(count_tuple[0], count_tuple[1]))
        
        
    group_chats_counts = filter(lambda count_tuple : count_tuple[2], counts)
    group_chats_counts = sorted(group_chats_counts, key = lambda count_tuple : count_tuple[1], reverse = True)
    output_list2 = []
    
    for count_tuple in group_chats_counts[:10]:
        output_list2.append("{}: {}".format(count_tuple[0], count_tuple[1]))
    
    return (output_list1, output_list2)
        