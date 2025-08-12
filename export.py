'''Script for exporting data from Wikidata for BosBWL'''
import pywikibot
import pandas as pd

ALL_PROPS = ['P31', 'P569', 'P19', 'P106', 'P570', 'P20', 'P101', 'P69', 'P21', 'P172', 'P27', 'P735', 'P734', 'P551', 'P1412', 'P800', 'P166', 'P463', 'P39', 'P737', 'P1343', 'P5008', 'P935', 'P119', 'P767', 'P26', 'P40', 'P25', 'P22', 'P3373', 'P742', 'P1449', 'P511', 'P1035', 'P1416', 'P485', 'P9600', 'P8258']
IDS = [
    'Q257911', 'Q274590', 'Q371930', 'Q466966', 'Q512065', 'Q520522', 'Q944063', 'Q3375368',
    'Q3381321', 'Q3634688', 'Q4754995', 'Q4766456', 'Q4793395', 'Q4793563', 'Q4793834', 'Q4794162',
    'Q5085940', 'Q5085958', 'Q5219331', 'Q5248354', 'Q5271705', 'Q5271708', 'Q5366368', 'Q5416490',
    'Q5433943', 'Q5571380', 'Q5623430', 'Q6116433', 'Q6205533', 'Q6288450', 'Q6487034', 'Q6761375',
    'Q6779398', 'Q6792212', 'Q6962698', 'Q7155037', 'Q7382891', 'Q7382962', 'Q7421686', 'Q11722350',
    'Q13560246', 'Q13562359', 'Q14948836', 'Q14954671', 'Q15488405', 'Q16013686', 'Q16065540', 'Q16975644',
    'Q17386048', 'Q17402931', 'Q18528650', 'Q18631985', 'Q19609948', 'Q19668086', 'Q19867576', 'Q21996939',
    'Q22018527', 'Q22338526', 'Q23498304', 'Q23772448', 'Q24965334', 'Q27662379', 'Q27974863', 'Q28209377',
    'Q28528823', 'Q22341391', 'Q23035643', 'Q28673746', 'Q28746249', 'Q28755558', 'Q28804310', 'Q29075901',
    'Q29453022', 'Q43388384', 'Q47537421', 'Q47541808', 'Q49209360', 'Q49808724', 'Q49923305', 'Q50059224',
    'Q50825734', 'Q51426289', 'Q59656431', 'Q59722180', 'Q59850604', 'Q62284560', 'Q64853061', 'Q70494400',
    'Q88385471', 'Q89355893', 'Q89912173', 'Q94134547', 'Q94683874', 'Q96255979', 'Q96746960', 'Q102820715',
    'Q102820775', 'Q107193074', 'Q108203888', 'Q108320604', 'Q108322941', 'Q108430984', 'Q108438101', 'Q108528937',
    'Q108755841', 'Q109463912', 'Q111577455', 'Q124396195', 'Q125516148', 'Q125516155', 'Q125516153', 'Q125516183',
    'Q125516187', 'Q125516195', 'Q125516201', 'Q125516209', 'Q125516262', 'Q130296842', 'Q131985856', 'Q132132927',
    'Q132178196', 'Q132178356', 'Q132200933', 'Q132200982', 'Q132201200', 'Q132201345', 'Q132316222', 'Q132318223',
    'Q132528973', 'Q132529038', 'Q132530218', 'Q132531745', 'Q132531858', 'Q132597624', 'Q132599469', 'Q132601586',
    'Q132603799', 'Q132606122', 'Q132607026', 'Q132607877', 'Q132608449', 'Q132609075', 'Q132616192', 'Q132737761',
    'Q132738312', 'Q132738745', 'Q132739333', 'Q132746575', 'Q132746654', 'Q132747827', 'Q132748409', 'Q132749051',
    'Q133259540', 'Q133259816', 'Q133260084', 'Q133273063', 'Q133273105', 'Q133273133', 'Q133782016', 'Q133810397',
    'Q133810458', 'Q133818868', 'Q133818892', 'Q133818924', 'Q133834715', 'Q133834733', 'Q133834777', 'Q133838225',
    'Q133857218', 'Q133862029', 'Q133862160', 'Q133862247', 'Q133862502', 'Q133862509', 'Q133862514', 'Q133862534',
    'Q133862554', 'Q125505143', 'Q133862562', 'Q133866956', 'Q133867053', 'Q133867172', 'Q133867180', 'Q133867187',
    'Q133867273', 'Q133867277', 'Q133871465', 'Q133871507', 'Q133871904', 'Q133872083', 'Q133872101', 'Q133872148',
    'Q133872209', 'Q133872232', 'Q133872361', 'Q133872382', 'Q134506481', 'Q134573639', 'Q135446152'
]
COLUMN_NAMES = [
    'identifier', 'link', 'label', 'description', 'alias',
    'instance of', 'instance of - notes',
    'honorific prefix', 'honorific prefix - notes',
    'family name', 'family name - notes',
    'given name', 'given name - notes',
    'honorific suffix', 'honorific suffix - notes',
    'pseudonym', 'pseudonym - notes',
    'nickname', 'nickname - notes',
    'date of birth', 'date of birth - notes',
    'place of birth', 'place of birth - notes',
    'date of death', 'date of death - notes',
    'place of death', 'place of death - notes',
    'place of burial', 'place of burial - notes',
    'sex or gender', 'sex or gender - notes',
    'ethnic group', 'ethnic group - notes',
    'country of citizenship', 'country of citizenship - notes',
    'languages', 'languages - notes',
    'occupation', 'occupation - notes',
    'field of work', 'field of work - notes',
    'educated at', 'educated at - notes',
    'residence', 'residence - notes',
    'notable work', 'notable work - notes',
    'award received', 'award received - notes',
    'member of', 'member of - notes',
    'position held', 'position held - notes',
    'affiliation', 'affiliation - notes',
    'archives at', 'archives at - notes',
    'oral history at', 'oral history at - notes',
    'field of training', 'field of training - notes',
    'influenced by', 'influenced by - notes',
    'described by source', 'described by source - notes',
    'on wikimedia project', 'on wikimedia project - notes',
    'commons gallery', 'commons gallery - notes',
    'contributor to work', 'contributor to work - notes',
    'spouse', 'spouse - notes',
    'child', 'child - notes',
    'mother', 'mother - notes',
    'father', 'father - notes',
    'sibling', 'sibling - notes'
]

def labeler(wd_id, repo):
    '''Script to grab labels from items and properties'''
    if 'P' in wd_id:
        property_page = pywikibot.PropertyPage(repo, wd_id).get()['labels'].toJSON()
        return ((property_page.get('en') or {}).get('value') or (property_page.get('mul') or {}).get('value') or next(iter(property_page))['value'])
    elif 'Q' in wd_id:
        item_page = pywikibot.ItemPage(repo, wd_id).get()['labels'].toJSON()
        return ((item_page.get('en') or {}).get('value') or (item_page.get('mul') or {}).get('value') or next(iter(item_page))['value'])
    
def wikidata_time_to_iso(ts):
    '''Script that converts timestamps'''
    if not ts or len(ts) < 18:
        return ""
    # Splicing time stamp
    year_str = ts[1:12]     # 1 to 11 (11 chars)
    month_str = ts[13:15]   # 13 and 14 (2 chars)
    day_str = ts[16:18]     # 16 and 17 (2 chars)

    try:
        year = int(year_str)
    except ValueError:
        return ""

    if month_str == "00":
        return f"{year:04d}"

    if day_str == "00":
        return f"{year:04d}-{month_str}"

    return f"{year:04d}-{month_str}-{day_str}"

def export_item(repo, q_id):
    print(q_id)
    # Create dictionary for new row
    row = dict.fromkeys(COLUMN_NAMES)
    item = pywikibot.ItemPage(repo, q_id)  # a repository item
    data = item.get()  # get all item data from repository for this item
    label = data['labels'].toJSON()
    description = data['descriptions'].toJSON()
    alias = data['aliases'].toJSON()
    claims = data['claims'].toJSON()
    row['identifier'] = q_id
    row['link'] = 'https://www.wikidata.org/entity/' + q_id
    row['label'] = (label.get('en') or {}).get('value')
    row['description'] = (description.get('en') or {}).get('value')
    aliases = (alias.get('en') or [{}])
    combined_aliases = '|'.join([a.get('value', '') for a in aliases if a.get('value')])
    row['alias'] = combined_aliases
    
    for p_value in claims:
        statement_lst = []
        notes_lst = []
        if p_value in ALL_PROPS:
            # print('-------------------------------------------------------------')
            print(p_value)
            property = labeler(p_value,repo)
            statement_counter = 0
            for statement in claims[p_value]:
                statement_counter += 1
                # print('statement ' + str(statement_counter))
                value = statement['mainsnak']['datavalue']['value']
                # check if it references another Wikidata item
                if 'numeric-id' in value and isinstance(value, dict):
                    statement_lst.append(labeler('Q' + str(value['numeric-id']), repo))
                    # print(labeler('Q' + str(value['numeric-id']), repo))
                # otherwise it's a definite time field
                elif 'time' in value and isinstance(value, dict):
                    statement_lst.append(wikidata_time_to_iso(value['time']))
                    # print(wikidata_time_to_iso(value['time']))
                else:
                    statement_lst.append(value)
                if 'references' in statement:
                    # Iterate over references
                    reference_counter = 1
                    for ref in statement['references']:
                        notes_lst.append('statement ' + str(statement_counter) + ', reference ' + str(reference_counter))
                        reference_counter += 1
                        # Iterate over each part of a reference
                        for part in ref['snaks']:
                            ref_label = labeler(ref['snaks'][part][0]['property'], repo)
                            reference = ref['snaks'][part][0]['datavalue']['value']
                        # print(ref['snaks'])
                        # ref_label = labeler(ref['snaks'][next(iter(ref['snaks']))][0]['property'], repo)
                        # reference = ref['snaks'][next(iter(ref['snaks']))][0]['datavalue']['value']
                        # if it references another Wikidata item
                            print(reference)
                            if 'numeric-id' in reference:
                                notes_lst.append(ref_label + ': ' + labeler('Q' + str(reference['numeric-id']), repo))
                                # print(ref_label + ': ' + labeler('Q' + str(reference['numeric-id']), repo))
                            # otherwise it's a definite time field
                            elif 'time' in reference and isinstance(reference, dict):
                                notes_lst.append(ref_label + ': ' + wikidata_time_to_iso(reference['time']))
                            elif 'text' in reference and isinstance(reference, dict):
                                notes_lst.append(ref_label + ': ' + reference['text'])
                            else:
                                notes_lst.append(ref_label + ': ' + reference)
                                # print(ref_label + ': ' + reference)
                        notes_lst.append('-----------------------------')
                if 'qualifiers' in statement:
                    qualifiers = statement['qualifiers']
                    qualifier_counter = 1
                    for qua in qualifiers:
                        notes_lst.append('statement ' + str(statement_counter) + ', qualifier ' + str(qualifier_counter))
                        qualifier_counter += 1
                        qua_label = labeler(qualifiers[qua][0]['property'], repo)
                        qualifier = qualifiers[qua][0]['datavalue']['value']
                        if isinstance(qualifier, dict):
                            if 'numeric-id' in qualifier:
                                notes_lst.append(qua_label + ': ' + labeler('Q' + str(qualifier['numeric-id']), repo))
                                # print(qua_label + ': ' + labeler('Q' + str(qualifier['numeric-id']), repo))
                            elif 'time' in qualifier:
                                notes_lst.append(qua_label + ': ' + wikidata_time_to_iso(qualifier['time']))
                                # print(qua_label + ': ' + wikidata_time_to_iso(qualifier['time']))
                        else:
                            notes_lst.append(qua_label + ': ' + qualifier)
                            # print(qua_label + ': ' + qualifier)
                        notes_lst.append('-----------------------------')
            row[property] = '|'.join(statement_lst)
            row[property + ' - notes'] = '\n'.join(notes_lst)

    return row

def main():
    """
    Main function for exporting BosBWL wikidata items
    """
    # initialize pywikibot
    site = pywikibot.Site('wikipedia:en')
    repo = site.data_repository() 
    # create df
    df = pd.DataFrame(columns=COLUMN_NAMES)
    for id in IDS[:10]:
        row = export_item(repo, id)
        df.loc[len(df)] = row
    df.to_csv('export.csv')

    

if __name__ == "__main__":
    main()