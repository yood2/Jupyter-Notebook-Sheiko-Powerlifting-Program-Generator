import pandas as pd

def render_beginner(squat,bench,deadlift):
    week1 = [[{"Squat":[squat*0.5,squat*0.6,squat*0.7,squat*0.7,squat*0.7,squat*0.7],"Reps":[5,5,4,4,4,4]},
            {"Bench":[bench*0.5,bench*0.6,bench*0.7,bench*0.75,bench*0.75,bench*0.75,bench*0.75],"Reps":[5,4,3,3,3,3,3]},
            {"Chest Accessory":['','','',''],"Reps":[8,8,8,8]}],

           [{"Deadlift":[deadlift*0.5,deadlift*0.6,deadlift*0.7,deadlift*0.75,deadlift*0.75,deadlift*0.75,deadlift*0.75],"Reps":[3,3,3,2,2,2,2]},
            {"Incline Bench Press":['','','','',''],"Reps":[3,3,3,3,3]},
            {"Seated Rows":['','','','',''],"Reps":[8,8,8,8,8]},
            {"Box Deadlift":[deadlift*0.55,deadlift*0.65,deadlift*0.75,deadlift*0.85,deadlift*0.85,deadlift*0.85],"Reps":[3,3,3,2,2,2]},
            {"Ab Accessory":['','',''],"Reps":[10,10,10]}],

           [{"Squat":[squat*0.5,squat*0.6,squat*0.7,squat*0.75,squat*0.75,squat*0.75,squat*0.75],"Reps":[5,4,3,3,3,3,3]},
            {"Bench":[bench*0.5,bench*0.6,bench*0.7,bench*0.8,bench*0.8,bench*0.8,bench*0.8],"Reps":[5,4,3,2,2,2,2]},
            {"Chest Accessory":['','','',''],"Reps":[8,8,8,8]},
            {"Triceps":['','','',''],"Reps":[6,6,6,6]},
            {"Good Morning":['','','','',''],"Reps":[5,5,5,5,5]}]
          ]

    print("Week 1")
    day_count = 1
    for day in week1:
        print(f"Day {day_count}")
        day_df = pd.DataFrame()
        for exercise in day:
            exercise_df = pd.DataFrame(exercise)
            day_df = pd.concat([day_df, exercise_df],axis=1)
        print(day_df)
        day_count += 1
        print("\n\n\n")
  
    week2 = [[{"Squat":[squat*0.5,squat*0.6,squat*0.7,squat*0.8,squat*0.8,squat*0.8,squat*0.8],"Reps":[5,4,3,2,2,2,2]},
            {"Bench":[bench*0.5,bench*0.6,bench*0.7,bench*0.8,bench*0.8,bench*0.8,bench*0.8,bench*0.8],"Reps":[5,4,3,3,3,3,3,3]},
            {"Lat Accessory":['','','',''],"Reps":[8,8,8,8]},
            {"Dips":['','','',''],"Reps":[6,6,6,6]},
            {"Back Extension":['','','',''],"Reps":[8,8,8,8]}
           ],

           [{"Deadlift":[deadlift*0.5,deadlift*0.6,deadlift*0.7,deadlift*0.75,deadlift*0.75,deadlift*0.75,deadlift*0.75],"Reps":[3,3,3,2,2,2,2]},
            {"Bench":[bench*0.5,bench*0.6,bench*0.65,bench*0.65,bench*0.65,bench*0.65],"Reps":[6,6,6,6,6,6]},
            {"Box Deadlift":[deadlift*0.55,deadlift*0.65,deadlift*0.75,deadlift*0.75,deadlift*0.75,deadlift*0.75],"Reps":[4,4,4,4,4,4]},
            {"Chest Accessory":['','','',''],"Reps":[8,8,8,8]},
            {"Delt Accessory":['','','',''],"Reps":[6,6,6,6]}
           ],

           [{"Squat":[squat*0.5,squat*0.6,squat*0.7,squat*0.7,squat*0.7,squat*0.7],"Reps":[5,5,4,4,4,4]},
            {"Close Grip Bench":[bench*0.5,bench*0.6,bench*0.7,bench*0.7,bench*0.7,bench*0.7],"Reps":[3,3,3,3,3,3]},
            {"Seated Row":['','','',''],"Reps":[8,8,8,8]},
            {"Tricep Accessory":['','','',''],"Reps":[8,8,8,8]},
            {"Back Extension":['','','',''],"Reps":[8,8,8,8]}
           ]
          ]
  
    print("Week 2")
    day_count = 1
    for day in week2:
        print(f"Day {day_count}")
        day_df = pd.DataFrame()
        for exercise in day:
            exercise_df = pd.DataFrame(exercise)
            day_df = pd.concat([day_df, exercise_df],axis=1)
        print(day_df)
        day_count += 1
        print("\n\n\n")
  
    week3 = [[{"Squat":[squat*0.5,squat*0.6,squat*0.7,squat*0.75,squat*0.75,squat*0.75,squat*0.75],"Reps":[5,4,3,3,3,3,3]},
            {"Bench":[bench*0.5,bench*0.6,bench*0.7,bench*0.8,bench*0.8,bench*0.8,bench*0.8,bench*0.8],"Reps":[5,4,3,2,2,2,2,2]},
            {"Chest Accessory":['','','',''],"Reps":[8,8,8,8]},
            {"DB Bench Press":['','','',''],"Reps":[6,6,6,6]},
            {"Good Morning":['','','','',''],"Reps":[5,5,5,5,5]}
           ],

           [{"Deficit Deadlift":[deadlift*0.5,deadlift*0.6,deadlift*0.65,deadlift*0.65,deadlift*0.65,deadlift*0.65],"Reps":[3,3,2,2,2,2]},
            {"Bench":[bench*0.5,bench*0.6,bench*0.7,bench*0.8,bench*0.8,bench*0.85,bench*0.85,bench*0.85],"Reps":[5,4,3,3,3,2,2,2]},
            {"Box Deadlift":[deadlift*0.6,deadlift*0.7,deadlift*0.8,deadlift*0.8,deadlift*0.9,deadlift*0.9,deadlift*0.9],"Reps":[3,3,3,3,2,2,2]},
            {"Seated Rows":['','','',''],"Reps":[6,6,6,6]},
            {"Abs Accessory":['','',''],"Reps":[10,10,10]}
           ],

           [{"Squat":[squat*0.5,squat*0.6,squat*0.7,squat*0.8,squat*0.8,squat*0.8,squat*0.8],"Reps":[5,4,3,2,2,2,2]},
            {"Decline Bench":[bench*0.5,bench*0.6,bench*0.7,bench*0.7,bench*0.7,bench*0.7],"Reps":[4,4,4,4,4,4]},
            {"Chest Accessory":['','','',''],"Reps":[8,8,8,8]},
            {"Tricep Accessory":['','','',''],"Reps":[8,8,8,8]}
           ]
          ]
  
    print("Week 3")
    day_count = 1
    for day in week3:
        print(f"Day {day_count}")
        day_df = pd.DataFrame()
        for exercise in day:
            exercise_df = pd.DataFrame(exercise)
            day_df = pd.concat([day_df, exercise_df],axis=1)
        print(day_df)
        day_count += 1
        print("\n\n\n")

    week4 = [[{"Squat":[squat*0.5,squat*0.6,squat*0.7,squat*0.8,squat*0.8,squat*0.85,squat*0.85,squat*0.85],"Reps":[5,4,3,2,2,2,2,2]},
            {"Bench":[bench*0.5,bench*0.6,bench*0.7,bench*0.8,bench*0.8,bench*0.8,bench*0.8,bench*0.8],"Reps":[5,4,3,3,3,3,3,3]},
            {"Lat Accessory":['','','',''],"Reps":[8,8,8,8]},
            {"DB Curls":['','','',''],"Reps":[6,6,6,6]},
            {"Back Extension":['','','',''],"Reps":[8,8,8,8]}
           ],

           [{"Bench":[bench*0.5,bench*0.6,bench*0.7,bench*0.8,bench*0.85,bench*0.85,bench*0.85,bench*0.85],"Reps":[5,4,3,3,2,2,2,2]},
            {"Pause Deadlift":[deadlift*0.5,deadlift*0.6,deadlift*0.7,deadlift*0.7,deadlift*0.75,deadlift*0.75,deadlift*0.75],"Reps":[2,2,2,2,1,1,1]},
            {"Chest Accessory":['','','',''],"Reps":[8,8,8,8]},
            {"Delt Accessory":['','','',''],"Reps":[6,6,6,6]},
            {"Abs Accessory":['','',''],"Reps":[10,10,10]}
           ],

           [{"Squat":[squat*0.5,squat*0.65,squat*0.75,squat*0.75,squat*0.75,squat*0.75],"Reps":[5,4,3,3,3,3]},
            {"Bench":[bench*0.5,bench*0.6,bench*0.7,bench*0.7,bench*0.7,bench*0.7],"Reps":[4,4,4,4,4,4]},
            {"Tricep Accessory":['','','',''],"Reps":[8,8,8,8]},
            {"Good Morning":['','','',''],"Reps":[5,5,5,5]}
           ]
          ]

    print("Week 4")
    day_count = 1
    for day in week4:
        print(f"Day {day_count}")
        day_df = pd.DataFrame()
        for exercise in day:
            exercise_df = pd.DataFrame(exercise)
            day_df = pd.concat([day_df, exercise_df],axis=1)
        print(day_df)
        day_count += 1
        print("\n\n\n")

def render_intermediate_small(squat,bench,deadlift):
    week1 = [[{"Squat":[squat*0.5,squat*0.6,squat*0.7,squat*0.7,squat*0.7,squat*0.7],"Reps":[5,4,3,3,3,3]},
              {"Bench":[bench*0.5,bench*0.6,bench*0.7,bench*0.7,bench*0.7,bench*0.7],"Reps":[4,4,4,4,4,4]},
              {"Chest Accessory":['','','',''],"Reps":[8,8,8,8]},
              {"Triceps":['','','','',''],"Reps":[6,6,6,6,6]},
              {"Good Morning":['','','',''],"Reps":[8,8,8,8]}],

             [{"Deadlift":[deadlift*0.5,deadlift*0.6,deadlift*0.7,deadlift*0.7,deadlift*0.7,deadlift*0.7],"Reps":[3,3,3,3,3,3]},
              {"Bench":[bench*0.5,bench*0.6,bench*0.7,bench*0.75,bench*0.75,bench*0.75,bench*0.75],"Reps":[5,4,3,2,2,2,2]},
              {"DB Bench Press":['','','','',''],"Reps":[5,5,5,5,5]},
              {"Lat Accessory":['','','','',''],"Reps":[8,8,8,8,8]},
              {"Ab Accessory":['','',''],"Reps":[10,10,10]}],

             [{"Squat":[squat*0.5,squat*0.6,squat*0.7,squat*0.7,squat*0.7,squat*0.7],"Reps":[4,4,4,4,4,4]},
              {"Bench":[bench*0.5,bench*0.6,bench*0.7,bench*0.75,bench*0.75,bench*0.75,bench*0.75],"Reps":[5,4,3,3,3,3,3]},
              {"Incline Bench Press":['','','',''],"Reps":[8,8,8,8]},
              {"Dips":['','','','',''],"Reps":[5,5,5,5,5]},
              {"Good Morning":['','','','',''],"Reps":[5,5,5,5,5]}
             ]
            ]
    
    print("Week 1")
    day_count = 1
    for day in week1:
        print(f"Day {day_count}")
        day_df = pd.DataFrame()
        for exercise in day:
            exercise_df = pd.DataFrame(exercise)
            day_df = pd.concat([day_df, exercise_df],axis=1)
        print(day_df)
        day_count += 1
        print("\n\n\n")

def main():
    render_intermediate_small(40,40,40)

if __name__ == "__main__":
    main()

