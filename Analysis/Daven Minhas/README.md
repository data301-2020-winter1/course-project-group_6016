**This file is for notes on progression of the lab**
*Daven Minhas*

**These milestones were worked on:**
1. miletone 1
2. milestone 2

**I could not get this code to run:**

This should be violinplot that shows "Make" on the bottom using hue to differentiate between bev and phev and display the amount of them sold. 

sns.violinplot(x="Make", y="Total_Make", hue="EV_Type", data=df, palette="Set2", split=True, scale="count")