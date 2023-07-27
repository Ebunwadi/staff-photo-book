from werkzeug.exceptions import Conflict,HTTPException,BadRequest, InternalServerError
from flask_restx import Resource, Namespace, fields
from models.dbModels import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
)
from flask import json, request, jsonify, make_response

auth_ns = Namespace("auth", description="A namespace for our Authentication")


signup_model = auth_ns.model(
    "SignUp",
    {
        "first_name": fields.String(),
        "email": fields.String(),
        "password": fields.String(),
        "last_name": fields.String(),
        "gender": fields.String(),
        "job_role": fields.String(),
        "address": fields.String(),
        "department": fields.String(),
        "is_admin": fields.Boolean(),
    },
)


login_model = auth_ns.model(
    "Login", {"email": fields.String(), "password": fields.String()}
)


@auth_ns.route("/signup")
class SignUp(Resource):
    @auth_ns.expect(signup_model)
    def post(self):
        data = request.get_json()

        email = data.get("email")

        db_user = User.query.filter_by(email=email).first()

        if db_user is not None:
            return make_response(jsonify({"error": f"email {email} already exists"}), 400)

        new_user = User(
            first_name=data.get("first_name"),
            email=data.get("email"),
            password=generate_password_hash(data.get("password")),
            last_name=data.get("last_name"),
            gender=data.get("gender"),
            address=data.get("address"),
            department=data.get("department"),
            job_role=data.get("job_role"),
            is_admin=data.get("is_admin"),
        )

        new_user.save()
        return make_response(jsonify({
            "message": "User created successfuly",
            "user": {
                "firstname": new_user.first_name,
                "email": new_user.email,
                "is_admin": new_user.is_admin,
            }
            }), 201)

@auth_ns.route("/login")
class Login(Resource):
    @auth_ns.expect(login_model)
    def post(self):
        data = request.get_json()

        email = data.get("email")
        password = data.get("password")

        db_user = User.query.filter_by(email=email).first()

        if db_user and check_password_hash(db_user.password, password):
            access_token = create_access_token(identity=db_user.email)
            refresh_token = create_refresh_token(identity=db_user.email)
            response = jsonify(
                { "status": "success",
                 "message": "login successful",
                 "access_token": access_token, 
                }
            )
            response.set_cookie('refresh_token', refresh_token)
            return response
        else:
            return make_response(jsonify({"message": "Invalid email or password"}), 400)
            # return make_response(jsonify({"error": "email  already exists"}), 400)


@auth_ns.route("/refresh")
class RefreshResource(Resource):
    @jwt_required(refresh=True)
    def post(self):
        refresh_token = request.cookies.get('refresh_token')
        print(refresh_token)
        if not refresh_token:
            return make_response(jsonify({"error": "unathourised"}), 401)
        
        current_user = get_jwt_identity()
        new_access_token = create_access_token(identity=current_user)

        return make_response(jsonify({"access_token": new_access_token}), 200)
    
@auth_ns.route("/logout")
class Logout(Resource):
    @jwt_required()
    def post(self):
        cookies = request.cookies.get('refresh_token')
        if not cookies:
            return make_response(jsonify({"error": "unathourised"}), 401)
        
        response = make_response(jsonify({"success": "logout successful"}), 200)
        response.set_cookie('refresh_token', '', expires=0)
        return response