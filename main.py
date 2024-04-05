import src.functions.user_functions as functions


def get_user(request):
    request_data = request.get_json()
    print(request_data)
    return functions.get_user(request_data["user_id"])
