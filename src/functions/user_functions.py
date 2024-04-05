from google.cloud import firestore



def get_user(request):
  firestore_client = firestore.Client(database='trading-helper-gcp')
  user_id = request.args.get('user_id')
  user_ref = firestore_client.collection('users').document(user_id)
  # Get the document snapshot
  user_snapshot = user_ref.get()

  # Check if the document exists
  if user_snapshot.exists:
    # Get the data from the snapshot
    user_data = user_snapshot.to_dict()
    return user_data
  else:
    print(f"No user found with ID: {user_id}")
    return None