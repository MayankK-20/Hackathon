# Hackathon

Epoch 5 hackathon was a 24 hour hackathon held on 15th March. <br>Over 1000 teams registered for it.<br><br>
<emphasis>

<i>We placed in top 5 for problem statement 4. </i></emphasis>
<br><br><br>***<br> <br> <br>
The 4th problem is based on setting a cost efficient and fair pipeline through a given city (in this case city of california).<br> <br>

Objective 1 : Focuses on setting the pipeline in the most efficient manner that is the least total distance of pipeline from all houses. <br>
We used gradient descent to first find out an initial fit for the line which was then optimised by iteratively checking for the optimal shift and optimal slope from the current line.<br> <br>

Objective 2 : Minimising the maximum distance of a house from the pipeline.<br>
Approach 1:<br>
In the code for Objective 1 we changed the condition from total distance to maximum distance from house.<br>
Approach 2:<br>
We can take a line then shift it towards the house with the maximum distance and keep on reducing the amount of shifts by which we get too a final line.<br> <br>

Objective 3 focused on finding multiple lines for the same problem.<br>
Used clusterring to get k lines.<br>
