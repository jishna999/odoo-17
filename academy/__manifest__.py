{
    'name': "academy",

    'summary': "Manage students, teachers, and hobbies effectively.",

    'description': """
        The Academy module helps manage students, teachers, hobbies, and student tags.
        It allows you to keep track of student information, assign hobbies, and categorize
        students using tags. Teachers can be linked to students, and all relevant information
        is organized and easily accessible.
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    'category': 'Education',
    'version': '0.1',
    'license': 'LGPL-3',

    'depends': ['base', 'mail', 'product'],

    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/hobbi.xml',
        'views/student_tag.xml',
        'views/student_tag_lines.xml',
        'views/student_tag_line_views.xml',
        'views/data.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
}
