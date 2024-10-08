FORM_CONFIGS = {
    1: {
        'title': 'Contact Form',
        'fields': [
            {'name': 'first_name', 'type': 'text', 'label': 'First Name'},
            {'name': 'last_name', 'type': 'text', 'label': 'Last Name'},
            {'name': 'email', 'type': 'email', 'label': 'Email'},
            {'name': 'message', 'type': 'textarea', 'label': 'Message'}
        ]
    },
    2: {
        'title': 'Feedback Form',
        'fields': [
            {'name': 'rating', 'type': 'number', 'label': 'Rating (1-5)'},
            {'name': 'comments', 'type': 'textarea', 'label': 'Comments'}
        ]
    },
    3: {
        'title': 'form_3',
        'fields': [
            {'name': 'full_Name', 'type': 'text', 'label': 'Full Name'},
            {'name': 'email', 'type': 'email', 'label': 'Email Id'},
            {'name': 'phone', 'type': 'number', 'label': 'Phone No'}
        ]
    },
}