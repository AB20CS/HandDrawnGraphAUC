# Area Under the Curve (AUC) of Hand-Drawn Graphs
An innovative solution for finding the area under the curve for hand-drawn graphs

## Solution
For the purposes of this demonstration, I will use a plot of blood pressures (similar to a record an anesthesiologist may keep during surgery). AUC of blood pressure readings is often a key measurement used in clinical research.

###### Step 1
Download [ImageJ](https://imagej.nih.gov/ij/download.html) distributed by the National Institutes of Health (NIH).

###### Step 2
Save the hand-drawn graph in `.png` format. Below is the graph to be used in this demonstration:
![image](https://user-images.githubusercontent.com/69637288/132969935-5aa4e47b-08b4-4c61-91f8-6d683c74b6d5.png)

###### Step 3
Open ImageJ and navigate to `Files` > `Open` and choose the `.png` file saved from Step 2.

###### Step 4
Click on the `Polygon selections` tool in the toolbar and draw a polygon on the opened image around the region whose area you wish to determine. Then, click `Analyze` > `Measure`.
![image](https://user-images.githubusercontent.com/69637288/132970023-1bd89bd4-e5f0-4ac9-a615-da0390618434.png)

###### Step 5
Click on the `Straight*, segmented or freehand lines` tool and draw a horizontal line across the width of the graph. Then, click `Analyze` > `Measure`.
![image](https://user-images.githubusercontent.com/69637288/132970500-54277c06-a716-4880-88cc-79f0bcce261c.png)

###### Step 6
Navigate to the `Results` window and press `Ctrl+S` on your keyboard and save the measurements as a `CSV` file. If there are multiple graphs, repeat Steps 2 to 6 and save the measurements for each subsequent graph in the same location. After all graph measurements have been saved, download `calculate_area.py` from this repository and save it in the same location as the saved `CSV` files. 
