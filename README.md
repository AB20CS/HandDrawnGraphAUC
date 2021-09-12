# Area Under the Curve (AUC) of Hand-Drawn Graphs
Often times, hand-drawn graphs need to be analyzed, but there is too much "noise" on the page for it be fed through an OCR software. Hence, a common alternative is to tediously record the coordinates of each individual point in a spreadsheet. This new solution reduces the hassle of having to parse through each individual data point and can exponentially speed up the time required to process larger amounts of data.

## Solution
_For the purposes of this demonstration, I will use a plot of blood pressures (similar to a record an anesthesiologist may keep during surgery). AUC of blood pressure readings is often a key measurement used to diagnose patients with hypotension/hypertension in clinical research._

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

###### Step 7
In the same way as the previous steps, take the following measurements:
- Area of a single unit square on the grid
- Length of a single unit square on the grid
These measurements will be used in Step 8.

###### Step 8
Run `calculate_area.py` via the terminal or the IDE of your choice and you will be prompted to enter the following parameters in the Console:
- Pixels per unit square: the area of a single unit square on the grid (measured in Step 7)
- Area per unit square: the area of each square in the units of the given context
  - In our example, the area per unit square is `5*10=50` since each unit width represents 5 minutes and each unit height represents 10 mm Hg.
- Value represented by each unit length: the value of each unit length in the given context.
  - In our example, this parameter is equal to `5`.
- Number of pixels per unit length: the length of a single unit square on the grid (measured in Step 7)
- Starting value on the y-axis: the y-value at the x-axis
  - In our example, this value is `50`.
After inputting the parameters, the rest of the program should run and the AUC value will be found in the `CSV` file with the name inputted by the user.
