commonList = ['0123456','123456789','picture1','password','12345678','111111',
           '123123','12345','1234567890','senha','1234567','qwerty','abc123',
           'Million2','000000','1234','iloveyou','aaron431','password1','qqww1122',
           '123','omgpop','123321','654321','qwertyuiop','qwer123456','123456a',
           'a123456','666666','asdfghjkl','ashley','987654321','unknown','zxcvbnm',
           '112233','chatbooks','20100728','123123123','princess','jacket025','evite',
           '123abc','123qwe','sunshine','121212','dragon','1q2w3e4r','5201314','159753',
           '123456789','pokemon','qwerty123','Bangbang123jobandtalent','monkey','1qaz2wsx',
           'abcd1234','default','aaaaaa','soccer','123654','ohmnamah23','12345678910',
           'zing','shadow','102030','11111111','asdfgh','147258369','qazwsx','qwe123',
           'michael','football','baseball','1q2w3e4r5t','party','daniel','asdasd','222222',
           'myspace1','asd123','555555','a123456789','888888','7777777','fuckyou','1234qwer',
           'superman','147258','999999','159357','love123','tigger','purple','samantha',
           'charlie','babygirl','88888888','jordan23','789456123','jordan','anhyeuem','killer',
           'basketball','michelle','1q2w3e','lol123','qwerty1','789456','6655321','nicole',
           'naruto','master','chocolate','maggie','computer','hannah','jessica','123456789a',
           'password123','hunter','686584','iloveyou1','987654321','justin','cookie','hello',
           'blink182','andrew','25251325','love','987654','bailey','princess1','123456',
           '101010','12341234','a801016','1111','1111111','anthony','yugioh','fuckyou1',
           'amanda','asdf1234','trustno1','butterfly','x4ivygA51F','iloveu','batman','starwars',
           'summer','michael1','00000000','lovely','jakcgt333','buster','jennifer','babygirl1',
           'family','456789','azerty','andrea','q1w2e3r4','qwer1234','hello123','10203',
           'matthew','pepper','12345a','letmein','joshua','131313','123456b','madison',
           'Sample123','777777','football1','jesus1','taylor','b123456','whatever','welcome',
           'ginger','flower','333333','1111111111','robert','samsung','a12345','loveme',
           'gabriel','alexander','cheese','passw0rd','142536','peanut','11223344','thomas','angel1']

pwd = input ("enter your password: ")

def isLength():
    if len(pwd) >= 8:
        print ("Your password passes the length test")
    else:
        print ("Your password is not atleast 8 characters in length")
isLength ()

def hasUpperCase():
    success = False
    for letter in pwd:
        if(letter.isupper()):
            success = True
    if (success == True):
        print(f"{pwd} has atleast one uppercase")
    else:
        print(f"{pwd} has no upper case")
hasUpperCase()

def hasLowerCase():
    success = False
    for letter in pwd:
        if(letter.islower()):
            success = True
    if success == True:
        print(f"{pwd} has atleast one lowercase")
    else:
        print(f"{pwd} has no lower case")
hasLowerCase()

def hasDigit():
    success = False
    for letter in pwd:
        if (letter.isnumeric()):
            success = True
    if success == True:
        print(f"{pwd} has atleast one number")
    else:
        print(f"{pwd} has no number in it")
hasDigit ()

def hasSymbol():
    if any(char in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_'] for char in pwd):
        print(f"{pwd} has atleast one symbol")
    else:
        print(f"{pwd} has no symbol in it")
hasSymbol()

def hasLessThan3():
    if len (pwd) < 3:
        print(f"{pwd} has less than 3 characters")
    else:
        print(f"{pwd} has 3 or more characters")
hasLessThan3()


def isCommon():
    if pwd in commonList:
        print(f"{pwd} is a common password")
    else:
        print(f"{pwd} is not a common password")
isCommon()