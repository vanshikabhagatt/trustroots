from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from authentication.models import (
    CustomUser,
    GrassrootProfile,
    DonorProfile,
    CommunityUserProfile,
)


class SignUpForm(UserCreationForm):
    # email = forms.EmailField(max_length=200, help_text="Required")
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}),)
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder" : "Email"}), required=False)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}) , max_length=16, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}) , max_length=16, required=True)
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

SDG_CHOICES = [
    ('', 'Select SDG'),
    ('No Poverty', 'No Poverty'),
    ('Zero Hunger', 'Zero Hunger'),
    ('Good Health and Well-being', 'Good Health and Well-being'),
    ('Quality Education', 'Quality Education'),
    ('Gender Equality', 'Gender Equality'),
    ('Clean Water and Sanitation', 'Clean Water and Sanitation'),
    ('Affordable and Clean Energy', 'Affordable and Clean Energy'),
    ('Decent Work and Economic Growth', 'Decent Work and Economic Growth'),
    ('Industry, Innovation and Infrastructure', 'Industry, Innovation and Infrastructure'),
    ('Reduced Inequality', 'Reduced Inequality'),
    ('Sustainable Cities and Communities', 'Sustainable Cities and Communities'),
    ('Responsible Consumption and Production', 'Responsible Consumption and Production'),
    ('Climate Action', 'Climate Action'),
    ('Life Below Water', 'Life Below Water'),
    ('Life on Land', 'Life on Land'),
    ('Peace and Justice Strong Institutions', 'Peace and Justice Strong Institutions'),
    ('Partnerships to achieve the Goal', 'Partnerships to achieve the Goal'),
]

class GrassrootProfileForm(forms.ModelForm):
    org_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Oganisation Name"}), max_length=30, required=True)
    description = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Describe Grassroot..."}))
    focus_area = forms.CharField(widget=forms.TextInput(attrs={"placeholder " : "Focus Area"}))
    contact_number = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": "Contact Number"}))
    location = forms.CharField(widget=forms.TextInput(attrs={"placeholder " : "Location"}))
    sdg = forms.ChoiceField(choices= SDG_CHOICES,widget=forms.Select(attrs={"placeholder" : "SDG"}))
    # profile_icon = forms.ImageField(widget=forms.FileInput(attrs={"placeholder": "Upload profile image"}), required=False)
    
    class Meta:
        model = GrassrootProfile
        fields = ("org_name", "description", "focus_area", "contact_number", "location", "sdg", "profile_icon")    


class DonorProfileForm(forms.ModelForm):
    fullName = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"FUll Name"}))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder" : "Phone Number"}))
    paymentMethod = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "Payment Method"}))
    firmName = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Firm Name"}))
    
    class Meta:
        model = DonorProfile
        fields = ("fullName", "phone", "paymentMethod", "firmName")


class CommunityUserProfileForm(forms.ModelForm):
    fullName = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"FUll Name"}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Age"}))
    location = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Location"}))

    class Meta:
        model = CommunityUserProfile
        fields = ("fullName", "age", "location")


# ---------------------------- Custom Login Forms ---------------------------- #
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )

    class Meta:
        fields = ("username", "password")


# class CustomUserCreationForm(UserCreationForm):
#     username = forms.CharField(
#         label="Username", max_length=50, help_text="Don't use special characters"
#     )
#     password1 = forms.CharField(label="Password")
#     password2 = forms.CharField(label="Confirm Password")
#     # password2 = forms.CharField(label="<PASSWORD>", widget=forms.PasswordInput

#     class Meta:
#         model = User
#         fields = ("username", "password1", "password2")
#         widgets = {
#             "username": forms.TextInput(attrs={"placeholder": "Username"}),
#             "password1": forms.PasswordInput(attrs={"placeholder": "Password"}),
#             "password2": forms.PasswordInput(attrs={"placeholder": "Confirm Password"}),
#         }
#         # widgets = {
#         #     "password1": forms.PasswordInput,
#         #     "password2": forms.PasswordInput,
#         # }
#         # labels = {
#         #     "username": "Username",
#         #     "password1": "Password",
#         #     "password2": "<PASSWORD>",
#         # }
#         # help_texts = {
#         #     "username": "Letters, digits and @/./+/-/_ only.",
#         #     "password1": "<PASSWORD>.",
#         #     "password2": "<PASSWORD>.",
#         # }
#         # error_messages = {
#         #     "username": {"unique": "A user with that username already exists."},
#         #     "password1": {
#         #         "min_length": "Your password must be at least 5 characters long."
#         #     },
#         #     "password2": {
#         #         "min_length": "Your password must be at least 5 characters long."
#         #     },
#         # }


# ---------------------------- Custom SignUp Form ---------------------------- #
# class CustomUserCreationForm(UserCreationForm):
#     username = forms.CharField(
#         widget=forms.TextInput(attrs={"placeholder": "Username"}),
#     )
#     password1 = forms.CharField(
#         widget=forms.TextInput(attrs={"placeholder": "Password"})
#     )
#     password2 = forms.CharField(
#         widget=forms.TextInput(attrs={"placeholder": "Cofirm the Password"})
#     )

#     class Meta:
#         model = User
#         fields = ("username", "password1", "password2")


# # ----------------------- Community User Creation Form ----------------------- #
# class CommunityUserCreationForm(CustomUserCreationForm):
#     fullName = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Full Name"}))
#     age = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder" : "Age"}))

#     class Meta(CustomUserCreationForm.Meta):
#         model = CommunityUser
#         fields = CustomUserCreationForm.Meta.fields + ("fullName",)


# # ----------------------- Donor User Creation Form ----------------------- #
# class DonorCreationForm(CustomUserCreationForm):
#     phone = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder": "Phone Number"}))
#     paymentMethod = forms.ChoiceField(widget=forms.TextInput(attrs={"placeholder": "Payment Method"}),)

#     class Meta(CustomUserCreationForm.Meta):
#         model = Donor
#         fields= CustomUserCreationForm.Meta.fields + ("phone", "paymentMethod")

# # ----------------------- Grassroot User Creation Form ----------------------- #
# class GrassrootUserCreationForm(CustomUserCreationForm):
#     orgName = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Organization Name"}),)
#     email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder" : "Email"}))

#     class Meta(CustomUserCreationForm.Meta):
#         model = Grassroot
#         fields = CustomUserCreationForm.Meta.fields + ("orgName", "email")
