import pandas as pd
import random
import string


def generateRandomPassword(n: int) -> str:
    """generate random password

    Args:
        n (int): 文字数

    Returns:
        str: ランダムな文字
    """

    random_list = [
        random.choice(string.ascii_letters + string.digits) for i in range(n)
    ]
    return "2024" + "".join(random_list)


def generateCSV(df: pd.DataFrame, filepath: str) -> None:
    """データフレームからcsvファイルを作成する

    Args:
        df (pd.DataFrame): データフレーム
        filepath (str): csvの出力先のパス
    """
    df.to_csv(path_or_buf=filepath)
    return None


def accountCreateBaseDataFrame() -> pd.DataFrame:
    """アカウントを作成する基盤データフレーム

    Returns:
        pd.DataFrame: データフレーム
    """
    return pd.DataFrame(
        {
            "名前 [displayName] 必須": [],
            "ユーザー名 [userPrincipalName] 必須": [],
            "初期パスワード [passwordProfile] 必須": [],
            "サインインのブロック (はい/いいえ) [accountEnabled] 必須": [],
            "名 [givenName]": [],
            "姓 [surname]": [],
            "役職 [jobTitle]": [],
            "部署 [department]": [],
            "利用場所 [usageLocation]": [],
            "番地 [streetAddress]": [],
            "都道府県 [state]": [],
            "国/リージョン [country]": [],
            "Office [physicalDeliveryOfficeName]": [],
            "市区町村 [city]": [],
            "郵便番号 [postalCode]": [],
            "会社電話 [telephoneNumber]": [],
            "携帯電話 [mobile]": [],
        }
    )


def accountAddGroupBaseDataFrame() -> pd.DataFrame:
    """アカウントをグループに追加する基盤データフレーム

    Returns:
        pd.DataFrame: データフレーム
    """
    return pd.DataFrame(
        {
            "メンバー オブジェクト ID またはユーザー プリンシパル名 [memberObjectIdOrUpn] 必須": []
        }
    )


def joinNewGuestAccount(
    base_df: pd.DataFrame, password: str, number: int
) -> pd.DataFrame:
    """アカウント作成データフレームに新しいゲストアカウントを追加する

    Args:
        base_df (pd.DataFrame): 追加先データフレーム
        password (str): パスワード
        number (int): アカウント名につける連番

    Returns:
        pd.DataFrame: 追加後のデータフレーム
    """

    data = pd.concat(
        [
            base_df,
            pd.DataFrame(
                {
                    "名前 [displayName] 必須": [f"2024_{number}_guest"],
                    "ユーザー名 [userPrincipalName] 必須": [
                        f"2024G{number}@seiryofes.com"
                    ],
                    "初期パスワード [passwordProfile] 必須": [password],
                    "サインインのブロック (はい/いいえ) [accountEnabled] 必須": ["No"],
                    "名 [givenName]": [None],
                    "姓 [surname]": [None],
                    "役職 [jobTitle]": [None],
                    "部署 [department]": [None],
                    "利用場所 [usageLocation]": [None],
                    "番地 [streetAddress]": [None],
                    "都道府県 [state]": [None],
                    "国/リージョン [country]": [None],
                    "Office [physicalDeliveryOfficeName]": [None],
                    "市区町村 [city]": [None],
                    "郵便番号 [postalCode]": [None],
                    "会社電話 [telephoneNumber]": [None],
                    "携帯電話 [mobile]": [None],
                }
            ),
        ]
    )

    return data


def joinNewAccount(
    base_df: pd.DataFrame, password: str, grade: int, room: int, number: int
) -> pd.DataFrame:
    """アカウント作成データフレームに新しいアカウントをデータフレームに追加する(CreateAccount用)

    Args:
        base_df (pd.DataFrame): 追加先データフレーム
        password (str): パスワード
        grade (int): 学年
        room (int): クラス
        number (int): 番号

    Returns:
        pd.DataFrame: 追加後のデータフレーム
    """

    if number < 10:
        data = pd.concat(
            [
                base_df,
                pd.DataFrame(
                    {
                        "名前 [displayName] 必須": [
                            f"2024_{grade}{room}0{number}_parent"
                        ],
                        "ユーザー名 [userPrincipalName] 必須": [
                            f"2024P{grade}{room}0{number}@seiryofes.com"
                        ],
                        "初期パスワード [passwordProfile] 必須": [password],
                        "サインインのブロック (はい/いいえ) [accountEnabled] 必須": [
                            "No"
                        ],
                        "名 [givenName]": [None],
                        "姓 [surname]": [None],
                        "役職 [jobTitle]": [None],
                        "部署 [department]": [None],
                        "利用場所 [usageLocation]": [None],
                        "番地 [streetAddress]": [None],
                        "都道府県 [state]": [None],
                        "国/リージョン [country]": [None],
                        "Office [physicalDeliveryOfficeName]": [None],
                        "市区町村 [city]": [None],
                        "郵便番号 [postalCode]": [None],
                        "会社電話 [telephoneNumber]": [None],
                        "携帯電話 [mobile]": [None],
                    }
                ),
            ]
        )

        return data
    else:
        data = pd.concat(
            [
                base_df,
                pd.DataFrame(
                    {
                        "名前 [displayName] 必須": [
                            f"2024_{grade}{room}{number}_parent"
                        ],
                        "ユーザー名 [userPrincipalName] 必須": [
                            f"2024P{grade}{room}{number}@seiryofes.com"
                        ],
                        "初期パスワード [passwordProfile] 必須": [password],
                        "サインインのブロック (はい/いいえ) [accountEnabled] 必須": [
                            "No"
                        ],
                        "名 [givenName]": [None],
                        "姓 [surname]": [None],
                        "役職 [jobTitle]": [None],
                        "部署 [department]": [None],
                        "利用場所 [usageLocation]": [None],
                        "番地 [streetAddress]": [None],
                        "都道府県 [state]": [None],
                        "国/リージョン [country]": [None],
                        "Office [physicalDeliveryOfficeName]": [None],
                        "市区町村 [city]": [None],
                        "郵便番号 [postalCode]": [None],
                        "会社電話 [telephoneNumber]": [None],
                        "携帯電話 [mobile]": [None],
                    }
                ),
            ]
        )

        return data


def joinGroupAccount(
    base_df: pd.DataFrame, grade: int, room: int, number: int
) -> pd.DataFrame:
    """基盤データフレームにアカウント情報を追加する(ImportGroup用)

    Args:
        base_df (pd.DataFrame): 基盤データフレーム
        grade (int): 学年
        room (int): ルーム
        number (int): 番号

    Returns:
        pd.DataFrame: 追加後のデータフレーム
    """
    if number < 10:
        data = pd.concat(
            [
                base_df,
                pd.DataFrame(
                    {
                        "メンバー オブジェクト ID またはユーザー プリンシパル名 [memberObjectIdOrUpn] 必須": [
                            f"2024P{grade}{room}0{number}@seiryofes.com"
                        ]
                    }
                ),
            ]
        )

        return data
    else:
        data = pd.concat(
            [
                base_df,
                pd.DataFrame(
                    {
                        "メンバー オブジェクト ID またはユーザー プリンシパル名 [memberObjectIdOrUpn] 必須": [
                            f"2024P{grade}{room}{number}@seiryofes.com"
                        ]
                    }
                ),
            ]
        )

        return data


def createParentsAccount() -> pd.DataFrame:
    """保護者アカウントを一括作成したデータフレームを作る

    Returns:
        pd.DataFrame: 保護者情報が載ったデータフレーム
    """

    # 全ての情報を入れるデータフレーム
    data = accountCreateBaseDataFrame()

    # 1 ~ 3 学年
    # rangeのstopは n → n - 1 まで繰り返す
    for m in range(1, 4):
        # 1 ~ 8 R
        for n in range(1, 9):
            for i in range(1, 45):
                data = joinNewAccount(data, generateRandomPassword(10), m, n, i)
    return data


def createGuestAccount(number: int, starts_at: int) -> pd.DataFrame:
    """ゲストアカウントを一括作成したデータフレームを作る

    Args:
        number (int): 何人分作るのか
        starts_at (int): 開始アカウント連番

    Returns:
        pd.DataFrame: ゲスト情報が乗ったデータフレーム
    """

    data = accountCreateBaseDataFrame()

    for i in range(starts_at, number + starts_at):
        data = joinNewGuestAccount(data, generateRandomPassword(15), i)

    return data


def addParentsGroup(grade: int, room: int) -> pd.DataFrame:
    """指定された学年の保護者をグループに追加するためのデータフレーム作成

    Args:
        grade (int): 学年
        room (int): ルーム

    Returns:
        pd.DataFrame: データフレーム
    """
    data = accountAddGroupBaseDataFrame()

    for n in range(1, 45):
        data = joinGroupAccount(data, grade, room, n)

    return data
