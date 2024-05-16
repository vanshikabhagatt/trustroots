from django.shortcuts import render, redirect, get_object_or_404
from authentication.models import GrassrootProfile, Follow
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse


# Create your views here.
def search_grassroot(request):
    if request.method == "POST":
        name = request.POST.get("gr-search-bar")
        grassroot = GrassrootProfile.objects.filter(org_name=name)
        context = {"grassroots": grassroot}
        return render(request, "grassroot/grassroots_page.html", context=context)
    # return redirect("base:grassrootPage")
    return HttpResponse("Not a post request")



def follow_grassroot(request, grassroot_id):
    if request.method == "POST":
        follower_user = request.user
        grassroot_to_follow = get_object_or_404(GrassrootProfile, user_id=grassroot_id)
        print("GRASSROOT : ")
        print(grassroot_to_follow)
        if grassroot_to_follow and request.user != grassroot_to_follow:
            Follow.objects.get_or_create(
                follower=request.user, following=grassroot_to_follow
            )
            # return redirect("base:grassroot_profile")
            return redirect(
                reverse("base:grassroot_profile", kwargs={"id": grassroot_id})
            )
        else:
            return HttpResponse("Something went wrong!")
    # return redirect("base:grassroot_profile")
    print("Not found post request")
    return redirect(reverse("base:grassroot_profile", kwargs={"id": grassroot_id}))


def unfollow_grassroot(request, id):
    follower = request.user
    following = get_object_or_404(GrassrootProfile, user_id=id)
    # print(following)
    obj = Follow.objects.get(follower=follower, following=following)
    if obj:
        obj.delete()
        print("Relation Deleted!")
        return redirect(reverse("base:grassroot_profile", kwargs={"id": id}))
    else:
        return redirect(reverse("base:grassroot_profile", kwargs={"id": id}))
