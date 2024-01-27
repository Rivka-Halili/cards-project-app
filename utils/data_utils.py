import pandas as pd
import random

def generate_mock_data(num_projects=12, max_stories=10):
    data = []
    for i in range(1, num_projects + 1):
        project_name = f"Project {i}"
        num_stories = random.randint(1, max_stories)
        for j in range(1, num_stories + 1):
            story_name = f"Story {j}"
            total = random.randint(1, 10)
            completed = random.randint(0, total)
            data.append([project_name, story_name, completed, total])

    df = pd.DataFrame(data, columns=['project_name', 'story_name', 'completed', 'total'])
    return df


def read_mock_data():
    data = generate_mock_data()
    grouped_data = data.groupby('project_name').apply(lambda x: x.to_dict('records')).to_dict()
    return grouped_data

