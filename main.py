from flask import Flask, request
from flask_restful import Api, Resource, reqparse
app = Flask(__name__)
api = Api(app)

userMessages= {
    "631880802": ['mess1', 'mess2', 'mess3'],
    "2": ['mess1', 'mess2', 'mess3'],
    "3": ['mess1', 'mess2', 'mess3'],
}
UsersentMessages = {

}

userPostArgs = reqparse.RequestParser()


messages_post_args = reqparse.RequestParser()
messages_post_args.add_argument("message", type=str, help="message is required", required=True)
# messages_post_args.add_argument("message_id", type=str, help="message ID is required", required=False)

class HelloWorld(Resource):
    def get(self):
        return {"data": "hello world"}
    
class Message(Resource):
    def get(self, user_id):
        # return {"userM": userMessages[f'{user_id}'] }, 200
        return{
            'messages' : UsersentMessages[user_id]
        }, 201
    
    def post(self, user_id):
        # args = messages_post_args.parse_args()
        # UsersentMessages[user_id] = args['message']``
        UsersentMessages[user_id] = request.json['message']
        # return {
        #     'message' : args['message'],
        #     'messageID': args['message_id'],
        #     'userID': f'{user_id}'
        #         }, 200
        return 'messages sent sucessfully to backend', 201
        # return {
        #     f'user messages with id {user_id}': args['messages']
        # }
        # return {
        #    "user sent messages":  UsersentMessages[user_id]
        # }, 201
        

# api.add_resource(HelloWorld, '/hello')
api.add_resource(Message, '/message/<int:user_id>')

if __name__ == "__main__":
    # add hosted url here using app.run()
    app.run(debug=True)
    
