# Hackathon

Epoch 5 hackathon was a 24 hour hackathon held on 15th March. <br>Over 1000 teams registered for it.<br><br>
<emphasis>

<i>We placed in top<b> 5</b> for problem statement 4. </i></emphasis>
<br><br><br>***<br> <br> <br>
The 4th problem is based on setting a <b>cost efficient and fair pipeline</b> through a given city (in this case city of California).<br> <br>

<h2>Objective 1 </h2> Focuses on setting the pipeline in the most efficient manner that is the least total distance of pipeline from all houses. <br><br>
We used gradient descent to first find out an initial fit for the line which was then optimised by iteratively checking for the optimal shift and optimal slope from the current line.<br> <br>

<h2>Objective 2 </h2> Minimising the maximum distance of a house from the pipeline.<br><br>
Approach 1: In the code for Objective 1 we changed the condition from total distance to maximum distance from house.<br>
Approach 2: We can take a line then shift it towards the house with the maximum distance and keep on reducing the amount of shifts by which we get too a final line.<br> <br>

<h2>Objective 3 </h2>Finding k lines that satisfy above conditions.<br><br>
We used k-means clustering to create k groups of points, in which the points within each group were close enough to each other. Consequently, to find the slope and intercept of the line for each cluster from which the total distance of those points is minimized, we used orthogonal regression. <br>
