heart_rate = 220


def fat_burning_heart_rate():
    user_heart_rate = (heart_rate - user_age) * 0.70
    print("Fat burning heart rate for a", user_age, "year-old:", '{0:.1f}'.format(user_heart_rate), "bpm")

def get_age():
    if user_age > 17 and user_age < 76:
        return user_age
    else:
        raise ValueError("Invalid age.")



if __name__ == '__main__':
    try:
        user_age = int(input())
        get_age()
        fat_burning_heart_rate()
    except ValueError:
        print("Invalid age.\nCould not calculate heart rate info.\n")
