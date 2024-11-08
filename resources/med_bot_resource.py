from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import jsonify

from bot import BotContextManager
from bot import MedBot
from schemas import MedBotSchema

blp = Blueprint('Med Bot Resource',
                __name__,
                description='Med Bot Resource APIs')


@blp.route('/medbot/<int:pid>')
class MedBotResource(MethodView):

    def get(self, pid):
        try:
            bot_context_manager = BotContextManager.get_instance()
            context = bot_context_manager.get_context(pid)
            return jsonify(context)

        except Exception as e:
            print(e)
            abort(500, message='Internal Server Error')

    @blp.arguments(MedBotSchema, location='json')
    def post(self, payload, pid):
        try:
            user_query = payload.get('user_query')

            bot_context_manager = BotContextManager.get_instance()
            med_bot = MedBot("creative")
            
            response = med_bot.get_response(user_query)
            if not response:
                return jsonify({"response": "Sorry, I am not able to understand."})
            
            bot_context_manager.update_context(
                pid,
                user_query,
                response.choices[0].message
            )
            return jsonify({"response": response})

        except Exception as e:
            print(e)
            abort(500, message='Internal Server Error')
