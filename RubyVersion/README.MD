This is currently for RPG Maker VX Ace games and converting relevent data into Wikia pages to be uploaded.

This is a work in progress to only require one script to run. It however required an .exe to be run to extract the initial data. The data such as weapon types isn't extracted yet, this will need to be found in the future.

I initially wrote this in python, however due to a lot of this initially being in Ruby, it makes sense for this to be rewritten in Ruby.

Step 1:     Backup the game files into another directory
Step 2:     Use the 'RPG_Maker_Resource_Project_Extractor' tool on the game files
Step 3:     The only files that are in the 'extract' folder are required
Step 4:     RVPacker is used to convert this to Ruby
