import requests

from configuration import SERVICE_URL

resp = requests.get(url=SERVICE_URL)

print(resp.json())

z = {
    'meta':
         {
             'pagination':
              {
                  'total': 2879,
                  'pages': 288,
                  'page': 1,
                  'limit': 10,
                  'links':
                    {
                        'previous': None,
                        'current': 'https://gorest.co.in/public/v1/users?page = 1',
                        'next': 'https://gorest.co.in/public/v1/users?page = 2'
                    }
               }
          },
     'data': [
         {
             'id': 4400595,
             'name': 'TrilokeshMenonJr.',
             'email': 'jr_trilokesh_menon @morissette - kunde.test',
             'gender': 'male',
             'status': 'active'
         },
         {
             'id': 4400593,
             'name': 'VedangaVarrier',
             'email': 'vedanga_varrier@donnelly.example',
             'gender': 'male',
             'status': 'active'
         },
         {
             'id': 4400592,
             'name': 'Gandharv Mukhopadhyay',
             'email': 'gandharv_mukhopadhyay@weber-vonrueden.test',
             'gender': 'female',
             'status': 'inactive'
         },
         {
             'id': 4400591,
             'name': 'Apsara Iyer',
             'email': 'apsara_iyer@bauch-botsford.example',
             'gender': 'female',
             'status': 'active'
         },
         {
             'id': 4400590,
             'name': 'Mr.Gopi Khatri',
             'email': 'khatri_mr_gopi@lubowitz.example',
             'gender': 'female',
             'status': 'inactive'
         },
         {
             'id': 4400589,
             'name': 'Deepankar Achari I',
             'email': 'deepankar_achari_i@krajcik.test', 
             'gender': 'male', 
             'status': 'inactive'
        }, 
        {
            'id': 4400588, 
            'name': 'HimaniDwivedi', 
            'email': 'dwivedihimani@schmitt.example', 
            'gender': 'female', 
            'status': 'active'
        }, 
        {
            'id': 4400587, 
            'name': 'RohanaMishra', 
            'email': 'mishra_rohana@mckenzie.example', 
            'gender': 'female', 
            'status': 'inactive'
        }, 
        {
            'id': 4400586, 
            'name': 'Rep.Hiranya Adiga', 
            'email': 'adiga_rep_hiranya @ nicolas.example', 
            'gender': 'male', 
            'status': 'inactive'
        }, 
        {
            'id': 4400585,
            'name': 'Sen. Devagya Embranthiri',
            'email': 'devagya_sen_embranthiri@cartwright.example',
            'gender': 'male',
            'status': 'active'
        }]
    }
