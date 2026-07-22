full_dot = '●'
empty_dot = '○'
def create_character(char_name,str_stat,int_stat,cha_stat):
    if not isinstance(char_name,str):
        return 'The character name should be a string'
    elif char_name == "":
        return 'The character should have a name'
    elif len(char_name)>10:
        return 'The character name is too long'
    elif ' ' in char_name:
        return 'The character name should not contain spaces'
    elif not isinstance(str_stat,int) or not isinstance(int_stat,int) or not isinstance(cha_stat,int):
        return 'All stats should be integers'
    elif str_stat<1 or int_stat<1 or cha_stat<1:
        return 'All stats should be no less than 1'
    elif str_stat>4 or int_stat>4 or cha_stat>4:
        return 'All stats should be no more than 4'
    elif (str_stat+int_stat+cha_stat) > 7 or (str_stat+int_stat+cha_stat) < 7:
        return 'The character should start with 7 points'
    else:
        str_value = full_dot*str_stat+empty_dot*(10-str_stat)
        int_value = full_dot*int_stat+empty_dot*(10-int_stat)
        cha_value = full_dot*cha_stat+empty_dot*(10-cha_stat)
        return f'\n{char_name}\nSTR {str_value}\nINT {int_value}\nCHA {cha_value}\n'

print(create_character(input("Enter the character name: "), int(input("Enter the strength stat (1-4): ")), int(input("Enter the intelligence stat (1-4): ")), int(input("Enter the charisma stat (1-4): "))))