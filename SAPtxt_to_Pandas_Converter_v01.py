# %%
# SAP TXT to Dataframe v1.0 10 aug 2021 by André Razera

# ======= Import Libraries ==========

import pandas as pd


# %%
def SAPtxtConverter(SAPtxtfilepath, col_line=4):

    """
    This function receives a txt file and convert it to a pandas dataframe
    
    SAPtxtfilepath = a txt file path that was saved from SAP. inform it without the txt extention
    col_line = inside the txt file, in which line is located the columns of the file. the default is 4 in case of txt files from tables without any filter
    obs: In this function the numbers are not converted
    by Andre Razera
    """   
    
    # ========= Read table txt raw file ================
    list1=[]
    textfile = open(SAPtxtfilepath+".txt", 'r') # Reads the file and make a list where every line of the txt is a register inside a list
    for line in textfile:
        list1.append(line)
    textfile.close()

    list2=[]   # Registers are splited by "|" signal, so now we use the split funcion to organize it inside the list
    for l in list1:
        list2.append(l.split("|"))

    # ========= Converting list into an structured pandas DataFrame ==============
    
    columns=list(pd.DataFrame(list2).iloc[col_line-1,col_line-2:-1].str.strip())  # get columns line, remove blank spaces
    data = pd.DataFrame(list2).iloc[col_line+1:,col_line-2:-1] # all txt files obey the same heading structure, so we can fix the lines and columns to search for data and columns 
    df = pd.DataFrame(data.values, columns=columns)

    return df


# %%
# ========= Example of function being called =========

df = SAPtxtConverter("ZA15_06_2021", 19) # with the need to configure the col_line attribute

df2 = SAPtxtConverter("ZA029H") # with the default col_line attribute


# %%
df2


# %%



