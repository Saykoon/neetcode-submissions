def remove_fourth_character(word: str) -> str:
    if len(word) > 4:
        before_4 = word[:3]
        after_4 = word[4:]
        new_message = before_4 + after_4
        return new_message
    else:
        return ""


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
