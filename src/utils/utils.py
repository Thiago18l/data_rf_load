# Mapping variables

def get_columns(class_name: str) -> dict:
    class_columns = {
        'Establishment': {
            0: 'taxpayerRegistry',
            1: 'cnpjOrder',
            2: 'cnpjDv',
            3: 'branchIdentifier',
            4: 'fantasyName',
            5: 'cadastralSituation',
            6: 'dateCadastralSituation',
            7: 'reasonCadastralSituation',
            8: 'outsideCityName',
            9: 'country',
            10: 'startDateActivity',
            11: 'principalCNAEFiscal',
            12: 'secondaryCNAEFiscal',
            13: 'typeOfStreet',
            14: 'street',
            15: 'number',
            16: 'complement',
            17: 'neighborhood',
            18: 'cep',
            19: 'UF',
            20: 'city',
            21: 'ddd1',
            22: 'phone1',
            23: 'ddd2',
            24: 'phone2',
            25: 'faxDDD',
            26: 'fax',
            27: 'email',
            28: 'especialSituation',
            29: 'dateSpecialSituation'
        },
        'Company': {
            0: 'taxpayerRegistry',
            1: 'businessName',
            2: 'legalNature',
            3: 'responsibleQualification',
            4: 'capitalCompany',
            5: 'sizeCompany',
            6: 'responsibleEntityFederative'
        },
        'Partner': {
            0: 'cnpjBasic',
            1: 'partnerIdentifier',
            2: 'partnerName',
            3: 'cpfOrCnpjPartner',
            4: 'partnerQualification',
            5: 'entryDataSociety',
            6: 'country',
            7: 'procurator',
            8: 'procuratorName',
            9: 'procuratorQualification',
            10: 'ageGroup'
        },
        'LegalNature': {
            0: 'code',
            1: 'description'
        },
        'QualificationPartner': {
            0: 'code',
            1: 'description'
        },
        'Country': {
            0: 'code',
            1: 'description'
        },
        'Cnae': {
            0: 'code',
            1: 'description'
        },
        'City': {
            0: 'code',
            1: 'description'
        }
        # adicionar outras classes e suas colunas aqui
    }
    if class_name in class_columns:
        return class_columns[class_name]
    else:
        raise ValueError(f'Classe {class_name} não é válida')


def get_dtypes(class_name: str) -> dict:

    dtypes_map = {
        'Company': {
            'taxpayerRegistry': 'object',
            'businessName': 'object',
            'legalNature': 'object',
            'responsibleQualification': 'object',
            'capitalCompany': 'object',
            'sizeCompany': 'object',
            'responsibleEntityFederative': 'object',
        },
        'Partner': {
            'cnpjBasic': 'object',
            'partnerIdentifier': 'object',
            'partnerName': 'object',
            'cpfOrCnpjPartner': 'object',
            'partnerQualification': 'object',
            'entryDataSociety': 'object',
            'country': 'object',
            'procurator': 'object',
            'procuratorName': 'object',
            'procuratorQualification': 'object',
            'ageGroup': 'object',
        },
        'Establishment': {
            'taxpayerRegistry': 'object',
            'cnpjOrder': 'object',
            'cnpjDv': 'object',
            'branchIdentifier': 'object',
            'fantasyName': 'object',
            'cadastralSituation': 'object',
            'dateCadastralSituation': 'object',
            'reasonCadastralSituation': 'object',
            'outsideCityName': 'object',
            'country': 'object',
            'startDateActivity': 'object',
            'principalCNAEFiscal': 'object',
            'secondaryCNAEFiscal': 'object',
            'typeOfStreet': 'object',
            'street': 'object',
            'number': 'object',
            'complement': 'object',
            'neighborhood': 'object',
            'cep': 'object',
            'UF': 'object',
            'city': 'object',
            'ddd1': 'object',
            'phone1': 'object',
            'ddd2': 'object',
            'phone2': 'object',
            'faxDDD': 'object',
            'fax': 'object',
            'email': 'object',
            'especialSituation': 'object',
            'dateSpecialSituation': 'object'
        },
        'LegalNature': {
            'code': 'object',
            'description': 'object'
        },
        'QualificationPartner': {
            'code': 'object',
            'description': 'object'
        },
        'Country': {
            'code': 'object',
            'description': 'object'
        },
        'Cnae': {
            'code': 'object',
            'description': 'object'
        },
        'City': {
            'code': 'object',
            'description': 'object'
        }
    }
    return dtypes_map.get(class_name, {})


dtypes = {
    'taxpayerRegistry': 'object',
    'cnpjOrder': 'object',
    'cnpjDv': 'object',
    'branchIdentifier': 'object',
    'fantasyName': 'object',
    'cadastralSituation': 'object',
    'dateCadastralSituation': 'object',
    'reasonCadastralSituation': 'object',
    'outsideCityName': 'object',
    'country': 'object',
    'startDateActivity': 'object',
    'principalCNAEFiscal': 'object',
    'secondaryCNAEFiscal': 'object',
    'typeOfStreet': 'object',
    'street': 'object',
    'number': 'object',
    'complement': 'object',
    'neighborhood': 'object',
    'cep': 'object',
    'UF': 'object',
    'city': 'object',
    'ddd1': 'object',
    'phone1': 'object',
    'ddd2': 'object',
    'phone2': 'object',
    'faxDDD': 'object',
    'fax': 'object',
    'email': 'object',
    'especialSituation': 'object',
    'dateSpecialSituation': 'object'
}
