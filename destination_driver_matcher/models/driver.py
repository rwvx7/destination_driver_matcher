
class Driver:
    """Class to represent a driver."""
    def __init__(self, data = {}):
        """
        params: data: dict()
        required to have the following keys:
        'name'
        """
        if not isinstance(data, dict):
            raise ValueError("'data' provided is not a string")
        self._name = data.get('name', None)
        self._cache = {}
    
    @property
    def name(self):
        return self._name

    def get_name_length(self):
        return len(self._name)

    def get_num_vowels_in_name(self):
        count = 0
        for ch in self._name.lower():
            if self._is_vowel(ch):
                count += 1
        return count

    def get_num_consonants_in_name(self):
        count = 0
        for ch in self._name.lower():
            if self._is_consonant(ch):
                count += 1
        return count


    def _is_consonant(self, ch):
        ch = ch.lower()
        return not (ch == 'a' or ch == 'e' or ch == 'i' or 
        ch == 'o' or ch == 'u') and ord(ch) >= 97 and ord(ch) <= 122

    def _is_vowel(self, ch):
        ch = ch.lower()
        return (ch == 'a' or ch == 'e' or ch == 'i' or 
        ch == 'o' or ch == 'u') and ord(ch) >= 97 and ord(ch) <= 122