# Stroop_Squared_in_PsychoPy
this is a PsychoPy implementation of the task designed by Burgoyne et al. (2023; https://doi.org/10.1037/xge0001408)

Stroop Squared Task, this is a PsychoPy implementation of the task designed by Burgoyne et al. (2023; https://doi.org/10.1037/xge0001408)

Running:
This experiment runs best in PsychoPy version 2021.2.3. Running it in other versions, especially on Mac, may cause difficulties. 
There are two different PsychoPy files: Stroop_Squared_color_only.psyexp and Stroop_Squared_all_3.psyexp. 
The  color_only version is implemented like in by Burgoyne et al. (2023), and is only one task. 
The all_3 version includes two novel types of Stroop squared task: an emotional task in which the words HAPPY and ANGRY are 
superimposed on happy or angry faces, and a gain\loss version where the words GAIN and LOSS are superimposed on stylized market charts with arrows 
denoting large gains or losses. 
After installing PsychoPy, find and open the desired .psyexp file in the folder. 

The output:
The most important columns in the output data file are:
color_word_final_score: This is the total amount of points earned during the color-word Stroop task. 
It does not include score from the practice session. This is the only output for the Stroop_Squared_color_only.psyexp file. 


emotion_final_score: This is the total amount of points earned during the emotion Stroop task. It does not include score from the practice session.


gain_loss_final_score: This is the total amount of points earned during the gain-loss Stroop task. It does not include score from the practice session.

Citation:
A preprint for this project is pending. If you wish to use this program, please cite the preprint when it is available. 

The task was originally conceptualized, designed, and validated by: 
Burgoyne, A. P., Tsukahara, J. S., Mashburn, C. A., Pak, R., & Engle, R. W. (2023). 
Nature and measurement of attention control. 
Journal of Experimental Psychology: General, 152(8), 2369–2402. 
https://doi.org/10.1037/xge0001408

, who should also be cited. 
