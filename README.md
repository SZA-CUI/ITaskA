# Time-Aware Semi-Supervised Routine Behavior Learning from Computer User Interaction Logs for Intelligent Task Assistance

This repository contains the source code and datasets for a time-aware semi-supervised framework designed to model routine behavior from computer users' personal interaction logs. The theoretical background of this work is presented in the paper *"Time-Aware Semi-Supervised Routine Behavior Learning from Computer User Interaction Logs for Intelligent Task Assistance"* by Ali, Seyyad Zishan and Mirza, Hamid Turab and Bilal, Ahmad and Hussain, Ibrar, currently under submission.

---

## 🔍 Project Objective

With the increasing need for intelligent desktop assistance systems, understanding user behavior from interaction logs has become essential. This project focuses on:

* Collection of raw desktop interaction log datasets
* Extraction of time-based activities from raw log entries
* Implementation of a semi-supervised learning approach for activity recognition
* Modeling routine user behavior using temporal and contextual features
* Development of predictive algorithms to assist users by forecasting their next possible desktop activity

---

## ⚠️ Challenges Addressed

* Desktop personal data logs are sensitive, making data collection difficult
* Extracting meaningful behavior from low-level interaction logs lacking semantic context
* Identifying periodic routine behaviors despite day-to-day variations
* Handling inconsistencies in repeated activities with varying temporal and contextual patterns
* Achieving accurate prediction of future activities from non-uniform behavioral data

---

## 📁 Dataset

**Description:**
Collection of raw desktop interaction logs was challenging due to privacy concerns, as users were hesitant to share personal activity data for certain periods. Participants were assured their data would be used strictly for research purposes, that enabled us to the voluntary engage of over 10 users. Similar with prior studies, key loggers were installed on participants’ systems to record their daily activities. Activity logging involves recording user desktop interactions into the log files. This dataset is built using:

* **User Activity Logger**: A desktop tool that records user-triggered events and actions
* **User-Classified Data**: Collected through daily activity record forms filled by users

**Data Availability:**: The dataset collected as a result of the proposed study is available in the current repository with file name "Users Personal Computer Interaction Logs.zip"

**Key Notes:**

* Logs capture detailed, low-level desktop activities
* User-provided labels support semi-supervised learning
* Due to privacy concerns, dataset sharing may be restricted or anonymized
* Behavioral patterns are preserved without exposing personal information

---

## 🧠 Project Structure and Execution Flow

| File Name                                     | Description                                                                   |
| --------------------------------------------- | ----------------------------------------------------------------------------- |
| `Users Personal Computer Interaction Logs`           |Contains the participated users' raw personal computer interaction logs and the survey forms filled by individual users for testing and training of the proposed research.  |
| `Required Libraries and Settings`             | Contains all necessary imports, environment configurations, and global constants.|
| `DATA CLEANSING AND PRE-PROCESSING`           | Cleans raw log data, removes noise, and prepares structured activity records. |
| `DAY CLASSIFICATION`                          | Classifies logs based on daily activity segmentation.                         |
| `ACTIVITY TIME CALCULATION`                   | Computes time spent on each activity from raw logs.                           |
| `ACTIVITY TIME SLOTTING`                      | Divides activities into predefined time slots for temporal analysis.          |
| `EACH SLOT ACTIVITY TIME CALCULATION`         | Calculates activity durations within each time slot.                          |
| `USER ACTIVITY CLASSIFICATION`                     | Applies semi-supervised learning to classify user activities.                 |
| `ONE DAY ACTIVITY MODELING`                   | Models user behavior for a single day.                                        |
| `ROUTINE ACTIVITY MODELING`                   | Aggregates daily models to learn long-term routine behavior patterns.         |
| `PREDICTION OF USER'S ROUTINE ACTIVITIES`     | Predicts future user activities based on learned patterns.                    |
| `Complete Application with GUI and integrated all steps` | End-to-end implementation with graphical interface for easy and as a whole execution of all steps through real-time interaction.      |

---

## 🔄 Execution Guide

1. **Install dependencies**:

   ```bash
   pip install -r Required Libraries and Settings.py
   ```

2. **Run data preprocessing**:

   ```bash
   python DATA_CLEANSING_AND_PRE_PROCESSING.py
   ```

3. **Classify data by day**:

   ```bash
   python DAY_CLASSIFICATION.py
   ```

4. **Calculate activity durations**:

   ```bash
   python ACTIVITY_TIME_CALCULATION.py
   ```

5. **Apply time slotting**:

   ```bash
   python ACTIVITY_TIME_SLOTTING.py
   ```

6. **Compute slot-wise activity time**:

   ```bash
   python EACH_SLOT_ACTIVITY_TIME_CALCULATION.py
   ```

7. **Perform activity classification**:

   ```bash
   python ACTIVITY_CLASSIFICATION.py
   ```

8. **Model daily behavior**:

   ```bash
   python ONE_DAY_ACTIVITY_MODELING.py
   ```

9. **Build routine behavior model**:

   ```bash
   python ROUTINE_ACTIVITY_MODELING.py
   ```

10. **Predict future activities**:

```bash
python PREDICTION_OF_USERS_ROUTINE_ACTIVITIES.py
```

11. **Run complete GUI application**:

```bash
python COMPLETE_APPLICATION_GUI.py
```

---

## ✅ Outputs

* Cleaned and structured desktop activity logs
* Time-based activity segmentation and slotting
* Semi-supervised classified user activities
* Daily and long-term routine behavior models
* Predicted next user activities for intelligent assistance
* End-to-end GUI-based system for one-time as a whole execution and interaction

---
## 🧪 Dataset Citation
If you use this work in your research, please cite the dataset:
```bash
Ali, S.Z. et al. (2026). Users Personal Computer Interaction Logs.zip. Github. URL: https://github.com/SZA-CUI/ITaskA
 ```
---
## 🧪 Research Work Citation

If you use this work in your research, please cite:

```bash
@article{zishanali2026ITaskA, 
  title     = {Time-Aware Semi-Supervised Routine Behavior Learning from Computer User Interaction logs for Intelligent Task Assistance}, 
  author    = {Ali, Seyyad Zishan and Mirza, Hamid Turab and Bilal, Ahmad and Hussain, Ibrar},
  journal   = {Under Submission},
  year      = {2026}, 
  note      = {\url{https://github.com/SZA-CUI/ITaskA}}
}
```
