#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 


# Author: Xiaoy Li
# Last update: 2019.04.29 
# First create: 2019.02.03  
# Description:
# query_map to produce query based NER 
# -------------------------------------------------------------- 
# Chinese and English Corpus involved in. 
# --------------------------------------------------------------
# English:
#   1. OntoNotes 5.0 
#   2. CoNLL 2003 
# Chinese:
#   1. MSRA (3) 人名，地名，机构名
#       * NS --- Location
#       * NR --- Personal Name
#       * NT  --- Organization
#   2. Resume (8)
#       * ORG --- Organization
#       * NAME --- Personal Name
#       * RACE --- Ethnicity Background 
#       * TITLE --- Job Title
#       * EDU --- Educational Institution
#       * LOC --- Location
#       * PRO --- Profession
#       * CONT --- Country
#   3. OntoNotes 5.0 (4)
#       * LOC --- Non-GPE locations, mountain ranges, bodies of water
#       * PER --- People, including fictional 
#       * GPE --- Countries, cities, states 
#       * ORG --- Organization
# ---------------------------------------------------------------------------------
# different query strategy can used in experiments 


import os
import sys

root_path = "/".join(os.path.realpath(__file__).split("/")[:-3])
if root_path not in sys.path:
    sys.path.insert(0, root_path)

    

en_onto_ner = {
    "tags": ['LAW', 'EVENT', 'CARDINAL', 'FAC', 'TIME', 'DATE', 'ORDINAL', 'ORG', 'QUANTITY',
             'PERCENT', 'WORK_OF_ART',
             'LOC', 'LANGUAGE', 'NORP', 'MONEY', 'PERSON', 'GPE', 'PRODUCT'],

    "natural_query": {
        "LAW": "named documents made into laws",
        "EVENT": "named hurricanes, battles, wars, sports events",
        "CARDINAL": "numerals that do not fall under another type",
        "FAC": "buildings, airports, highways, bridges, etc",
        "TIME": "times smaller than a day",
        "DATE": "absolute or relative dates or periods",
        "ORDINAL": "first or second",
        "ORG": "companies, agencies, institutions",
        "QUANTITY": "measurements, as of weight or distance",
        "PERCENT": "percentage including %",
        "WORK_OF_ART": "titles of books, songs",
        "LOC": "not geographical locations, mountain ranges, bodies of water",
        "LANGUAGE": "any named language",
        "NORP": "nationalities or religious or political groups",
        "MONEY": "monetary values, including unit",
        "PERSON": "people, including fictional",
        "GPE": "countries, cities, state",
        "PRODUCT": "vehicles, weapons, foods, etc. not services"
    },
    "psedo_query": {
        "LAW": "law",
        "EVENT": "event",
        "CARDINAL": "numeral",
        "FAC": "facility",
        "TIME": "time",
        "DATE": "date",
        "ORDINAL": "ordinal",
        "ORG": "organization",
        "QUANTITY": "quantity",
        "PERCENT": "percentage",
        "WORK_OF_ART": "title",
        "LOC": "location",
        "LANGUAGE": "language",
        "NORP": "group",
        "MONEY": "money",
        "PERSON": "person",
        "GPE": "geographical entity",
        "PRODUCT": "product"
    }
}

en_conll03_ner = {
    "tags": ["ORG", "PER", "LOC", "MISC"],
    "natural_query": {
        "ORG": "companies, agencies, institutions",
        "LOC": "not geographical locations, mountain ranges, bodies of water",
        "PER": "people, including fictional",
        "MISC": "miscellaneous entity"
    },
    "psedo_query": {
        "ORG": "organization",
        "PER": "person",
        "LOC": "location",
        "MISC": "miscellaneous entity"
    }
}

zh_msra_ner = {
    "tags": ["NS", "NR", "NT"],
    # new_1
    # "natural_query": {
    #     "NS": "国家，城市，山川等抽象或具体的地点",
    #     "NR": "真实和虚构的人名",
    #     "NT": "公司,商业机构,社会组织等组织机构"
    # },
    # new_2
    # "natural_query": {
    #     "NS": "国家，城市，州，山川，河流，海洋等抽象或具体的地点",
    #     "NR": "真实和虚构的人名",
    #     "NT": "公司,商业机构,社会组织，党派等组织机构"
    # },
    # new_3
    "natural_query": {
        "NS": "抽象和具体的地点",
        "NR": "真实和虚构的人名",
        "NT": "公司,党派等组织机构"
    },
    "psedo_query": {
        "NS": "地点",
        "NR": "人名",
        "NT": "组织机构"
    }
}

zh_onto_ner = {
    "tags": ["LOC", "PER", "GPE", "ORG"],
    "natural_query": {
        "LOC": "一",
        "PER": "二",
        "GPE": "三",
        "ORG": "四"
    },
    "psedo_query": {
        "LOC": "地点",
        "PER": "人名",
        "GPE": "位置",
        "ORG": "组织"
    }
}

zh_resume_ner = {
    "tags": ["ORG", "NAME", "RACE", "TITLE", "EDU", "LOC", "PRO", "CONT"],

    "psedo_query": {
        "ORG": "组织机构",
        "LOC": "地点",
        "NAME": "个名",
        "RACE": "种族背景",
        "TITLE": "工作职称",
        "EDU": "教育机构",
        "PRO": "职业专业",
        "CONT": "国家"
    }
}

# 自然的地点
zh_onto_ner_loc = {
    "tags": ["LOC"],
    "natural_query": {
        # "LOC": "山脉，水体等具体的地点",
        "LOC": "自然的地点",
    },
    "psedo_query": {
        "LOC": "具体的地点",
    }
}

zh_onto_ner_per = {
    "tags": ["PER"],
    "natural_query": {
        "PER": "人名，角色",
    },
    "psedo_query": {
        "PER": "人名",
    }
}

zh_onto_ner_gpe = {
    "tags": ["GPE"],
    "natural_query": {
        # "GPE": "抽象的地理位置",
        "GPE": "抽象的地点",
    },
    "psedo_query": {
        "GPE": "位置",
    }
}

zh_onto_ner_org = {
    "tags": ["ORG"],
    "natural_query": {
        "ORG": "公司,服务机构,社会组织"
    },
    "psedo_query": {
        "ORG": "组织机构"
    }
}

en_conll03_ner_org = {
    "tags": ["ORG"],
    "natural_query": {
        "ORG": "companies, agencies, institutions",
    },
}

zh_resume_ner = {
    "tags": ["ORG", "NAME", "RACE", "TITLE", "EDU", "LOC", "PRO", "CONT"],

    "natural_query": {
        "ORG": "组织或机构",
        "LOC": "地点",
        "NAME": "姓名",
        "RACE": "种族",
        "TITLE": "职称",
        "EDU": "教育机构",
        "PRO": "职业背景",
        "CONT": "国家"
    },
    "psedo_query": {
        "ORG": "组织",
        "LOC": "地点",
        "NAME": "姓名",
        "RACE": "种族",
        "TITLE": "职称",
        "EDU": "教育",
        "PRO": "职业",
        "CONT": "国家"
    }
}

genia_ner = {
    "tags": ['cell_line', 'cell_type', 'DNA', 'RNA', 'protein'],
    "natural_query": {
        'cell_line': "cell line",
        'cell_type': "cell type",
        'DNA': "DNA",
        'RNA': "RNA",
        'protein': "protein"
    },
    "psedo_query": 1
}

query_sign_map = {
    "en_onto_ner": en_onto_ner,
    "en_conll03_ner": en_conll03_ner,
    "en_conll03_ner_org": en_conll03_ner_org,
    "zh_msra_ner": zh_msra_ner,
    "zh_onto_ner": zh_onto_ner,
    "zh_onto_ner_loc": zh_onto_ner_loc,
    "zh_onto_ner_per": zh_onto_ner_per,
    "zh_onto_ner_gpe": zh_onto_ner_gpe,
    "zh_onto_ner_org": zh_onto_ner_org,
    "genia_ner": genia_ner,
    # "zh_resume_ner": zh_resume_ner
}
