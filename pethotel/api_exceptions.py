from fastapi import  HTTPException ,status

credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

invalid_data_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
    )

inactive_user =HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Inactive user"
            )

invalid_post_data  = HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Incorrect data , not supported by browser",
            headers={"WWW-Authenticate": "Bearer"},
    )
not_permitted = HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Operation not permitted")

not_found = HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="cannot find the data",
            headers={"WWW-Authenticate": "Bearer"},
    )

existing_user =HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="user already exists"
            )