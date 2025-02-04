# parking-spot-checker
A program to detect open parking spots in images of parking lots.

A YOLOv8 model is used to detect cars in the image. I trained the model's weights 
with a dataset of over 10k labelled parking lot images, collected from multiple
sources. 

There are several different versions of the model trained with different epoch and 
batch sizes, with their own strengths and weaknesses. 

## Examples:
### High Angle
<img src="readme_media/high_unprocessed.png" alt="High angle unprocessed image of parkin g lot" width="300"/>

The model works very well with images taken from a **high angle**, where the 
view is clear and the cars are easily distinguishable.

<img src="readme_media/high_processed.png" alt="High angle processed image of parking lot, every unoccupied parking spot is annotated" width="300"/>

**Green spaces** represent unoccupied parking spots.

### Lower Angle

<img src="readme_media/lower_unprocessed.png" alt="Lower angle unprocessed image of parking lot" width="300"/>

The model also works with images taken from a **lower angle**, where cars 
tend to obstruct the view of others

<img src="readme_media/lower_processed.png" alt="Lower angle processed image of parking lot, every parking spot is annotated" width="300"/>

### Large Parking Lots
<img src="readme_media/large_unprocessed.png" alt="Unprocessed image of large parking lot" width="300"/>

The model detects parking spots in images covering many spaces

<img src="readme_media/large_processed.png" alt="Processed mage of large parking lot, every parking spot is annotated" width="300"/>

## Dataset Credits

### **CNRPark+EXT Dataset**  
**Source:** [CNRPark](http://cnrpark.it/)  
**Citation:**  
Alfredo Paolanti, Paolo Zoppetti, Alessandro Pierdicca, Emanuele Frontoni,  
*"CNRPark+EXT: A Large Dataset for Parking Area and Parking Space Classification"*,  
*IEEE CVPRW*, 2018.  
**DOI:** [10.1109/CVPRW.2018.00009](https://doi.org/10.1109/CVPRW.2018.00009)  

---

### **DeteksiParkirKosong Dataset**  
**Author:** SkripsiJeremy  
**Type:** Open Source Dataset  
**Published on:** [Roboflow Universe](https://universe.roboflow.com/skripsijeremy/deteksiparkirkosong)  
**Publisher:** Roboflow  
**Year:** 2024 (September)  
**Accessed on:** February 4, 2025  

---

### **PKLot Dataset**  
**Title:** PKLot – A Robust Dataset for Parking Lot Classification  
**Authors:** Paulo R.L. de Almeida, Luiz S. Oliveira, Alceu S. Britto Jr., Eunelson J. Silva Jr., Alessandro L. Koerich  
**Published in:** *Expert Systems with Applications*, Volume 42, 2015, Pages 4937–4949  
**DOI:** [10.1016/j.eswa.2015.02.009](https://doi.org/10.1016/j.eswa.2015.02.009)  
**Dataset URL:** [http://web.inf.ufpr.br/vri/parking-lot-database](http://web.inf.ufpr.br/vri/parking-lot-database)  
