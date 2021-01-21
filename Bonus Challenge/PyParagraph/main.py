# Import CSV file
import os
txtpath = os.path.join("Resources", "pyparagraph_1.txt")

paragraph = []
par_str = []
par_str2 = []
par_list = []
par_list2 = []
word_count = []
sentence_count = []
letter_per_word = []
avg_letter_count = []
avg_letter_dec = []
avg_sentence_length = []
# Define punctuation 

with open(txtpath, "r") as tfile:

    # Put paragraph in paragraph
    for word in tfile:
        paragraph.append(word)

    # Convert list into string 
    par_str = str(paragraph)
    par_str2 = str(paragraph)

    # Define punctuation 
    punctuation = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    punctuation_sentence = '''!()-[]{};:'"\, <>/?@#$%^&*_~'''

    # Remove all punctuation
    for x in par_str:
        if x in punctuation:
            par_str = par_str.replace(x, " ")
    
    # Convert str to list  
    par_list = par_str.split()

    # Approximate word count 
    word_count = (len(par_list))

    # Sentence Count 
    # Remove all punctuation except for ( . ) 
    for i in par_str2:
        if i in punctuation_sentence:
            par_str2 = par_str2.replace(i, " ")


    # Convert str into list seperated by( . )  
    par_list2 = par_str2.split(".")

    # Count sentence 
    sentence_count = (len(par_list2))

    # Average letter count:
    for q in par_list:
        letter_per_word.append(len(q))
    total_letter = sum(letter_per_word)
    avg_letter_dec = total_letter / word_count
    avg_letter_count = "{:.2f}".format(avg_letter_dec) 

    # Average sentence length 
    avg_sentence_length = word_count / sentence_count 

    # Label every print 
    paragraph_analysis = ("Paragraph Analysis")
    dash = ("--------------------")
    awc = (f"Approximate Word Count: {word_count}")
    asc = (f"Approximate Sentence Count: {sentence_count}")
    alc = (f"Average Letter Count: {avg_letter_count}")
    asl = (f"Average Sentence Length: {avg_sentence_length} ")

# Print everything
print(paragraph_analysis)
print(dash)
print(awc)
print(asc)
print(alc)
print(asl)

# Compile print 
txtwrite = (paragraph_analysis,dash,awc,asc,alc,asl)


# Write to txt file 
output_path = os.path.join("analysis","analysis.txt")
with open(output_path, "w") as tfile:
    for a in txtwrite:
        tfile.write(a)
        tfile.write("\n")
        
