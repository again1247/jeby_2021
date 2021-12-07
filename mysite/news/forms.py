from django import forms


class NewsSearchForm(forms.Form):
    keyword = forms.CharField(max_length=100, required=True)


# 유효성 체크를 위해 Form을 적극 사용해야함!!
# forms.캐릭터필드로 하면 유효성 체크를 할수있고, 안맞으면 invalid로 떨어짐.
# 다양한 구현이 가능하다.
