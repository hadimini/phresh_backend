from fastapi import APIRouter, Path, Body

from app.models.profile import ProfileUpdate, ProfilePublic


router = APIRouter()


@router.get('/{username}/', response_model=ProfilePublic, name='profile:get-profile-by-username')
async def get_profile_by_username(
        *,
        username: str = Path(..., min_length=1, regex=r'^[a-zA-Z0-9_-]+$]'),
) -> ProfilePublic:
    return None


@router.put('/{username}/', response_model=ProfilePublic, name='profile:update-own-profile')
async def update_own_profile(
        profile_update: ProfileUpdate = Body(..., embed=True)
) -> ProfileUpdate:
    return None
