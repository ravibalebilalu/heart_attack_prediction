#  🫀 Heart Attack Prediction System 🫀

This app predicts possible heart attack risk by analyzing  health data.

## ⚠️ Disclaimer : 
### This app is created for educational purpose. Use of this app is at your own risk.  The author is not responsible for any consequences resulting from its use.
##  📊 Data for Prediction
### - **age** :  patient's age
### - **gender** : Gender, 0 for female ,1 for male
### - **heart_rate** : number of heartbeats per minute
### - **systolic_blood_pressure** : pressure in arteries when the heart contracts
### - **diastolic_blood_pressure** :  pressure in arteries between heartbeats
### - **blood_sugar** :  patient's blood glucose level
### - **ck-mb** :  cardiac enzyme released during heart muscle damage
### - **troponin** : highly specific protein biomarker for heart muscle injury

## Result : Output is either negative or positive depending on data supplied.



   ## data set  source : [Kaggle](https://www.kaggle.com/datasets/fatemehmohammadinia/heart-attack-dataset-tarik-a-rashid)


   ## 📚 Libraries  used

   1. pandas
   2. numpy
   3. sklearn
   4. pickle
   5. flask
   6. matplotlib
   7. seaborn

# 🛠️ How to run the app (Educational Use Only)

## 1. open up terminal

## 2. clone the repository 
   link : [heart_attack_prediction](https://github.com/ravibalebilalu/heart_attack_prediction.git)

   ```
   git clone  https://github.com/ravibalebilalu/heart_attack_prediction.git
   ```
##  3. Navigate into the project directory
```
cd heart_attack_prediction
```

## 4. create virtual environment and activate

```
python3 -m venv .heart
```
```
source .heart/bin/activate
```
## 5. install libreries

```
pip install -r requirements.txt
```

## 6. run app

```
python app.py
```
 Now open the IP address shown in terminal in your browser.
Fill the form with appropriate data to predict heart attack risk.

License :  [ Apache 2.0 License ](https://www.apache.org/licenses/LICENSE-2.0)
