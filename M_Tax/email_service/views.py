from django.shortcuts import redirect, render
from .models import Mail
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactUsForm

from django.utils.text import slugify
from django.db import IntegrityError


username = None
user_message=None
user_mobile=None
user_email=None


def generate_unique_slug(username):
    # Generate a base slug based on the username
    slug = slugify(username)
    
    # Check if the slug already exists in the database
    existing_slugs = Mail.objects.filter(slug=slug)
    
    # If the slug exists, add a number to make it unique
    count = 1
    while existing_slugs.exists():
        # Append a number to the slug and check again
        slug = f"{slugify(username)}-{count}"
        existing_slugs = Mail.objects.filter(slug=slug)
        count += 1
    
    return slug



def send_emails(request, user_email='None'):
    try:
        emails = Mail.objects.values_list('email', flat=True)  # Get all emails from Mail model
        subject = 'Thank You for Your Inquiry - We’re Here to Help!'

        for email in emails:
            if email == user_email:
                # Get the data for the specific email (user email)
                all_values = Mail.objects.filter(email=user_email).values()
                if not all_values:
                    raise ValueError(f"No data found for email: {user_email}")

                # Render HTML email content using the provided template
                message_html = render_to_string('mdottax/pages/email.html', {
                    'all_values': all_values,
                    'subject': subject,
                    'message': user_message,
                    'name': username,
                    'mobile':user_mobile,
                    'email':user_email

                })

                # Send the email
                send_mail(subject, user_message, None, [email], html_message=message_html)

    except Exception as e:
        print(f"Error while sending emails: {e}")
        # Handle error appropriately if needed

    return None

def contact_us(request):
    global username,user_message,user_mobile,user_email

    if request.method == 'POST':
        # Object for the form
        form = ContactUsForm(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                user_email = form.cleaned_data['email']
                user_mobile = form.cleaned_data['mobile']
                user_message = form.cleaned_data['message']

                 # Generate a unique slug for the new Mail object
                unique_slug = generate_unique_slug(username)

                # Create an instance of Mail (save it into DB in Mail Table)
                mail_instance = Mail(
                    name=username,
                    email=user_email,
                    slug=unique_slug,  # Use the dynamically generated unique slug
                    mobile=user_mobile,
                    message=user_message
                )

                # Save the instance to the database
                mail_instance.save()

                # Optionally, show success message
                success_message = f"Hello {username}, your query is received successfully! Our team will contact you shortly."
                messages.success(request, success_message)

                # Call function to send email
                send_emails(request, user_email)

                # Redirect to a success page
                return redirect('contact_us')

            except Exception as e:
                # Handle database or other exceptions and show error message
                error_message = f"Hello {username}, there was a problem with our database. Please try again later."
                messages.error(request, error_message)
                print(f"Error: {e}")  # For debugging purposes
        else:
            messages.error(request, "Form is not valid. Please check your inputs.")
    else:
        form = ContactUsForm()

    return render(request, 'mdottax/pages/contact_us.html', {'form': form})
