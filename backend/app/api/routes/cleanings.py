from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

from app.api.dependencies.database import get_repository
from app.db.repositories.cleanings import CleaningsRepository
from app.models.cleaning import CleaningCreate, CleaningPublic

router = APIRouter()


@router.get('/', response_model=List[CleaningPublic], name='cleanings:get-cleanings')
async def get_cleanings(
        cleanings_repo: CleaningsRepository = Depends(get_repository(CleaningsRepository))
) -> List[dict]:
    return await cleanings_repo.get_cleanings()


@router.post('/', response_model=CleaningPublic, name='cleanings:create-cleaning', status_code=HTTP_201_CREATED)
async def create_cleaning(
        new_cleaning: CleaningCreate = Body(..., embed=True),
        cleanings_repo: CleaningsRepository = Depends(get_repository(CleaningsRepository))
) -> CleaningPublic:
    created_cleaning = await cleanings_repo.create_cleaning(new_cleaning=new_cleaning)
    return created_cleaning


@router.get('/{id}/', response_model=CleaningPublic, name='cleanings:get-cleaning-by-id')
async def get_cleaning_by_id(
        id: int,
        cleanings_repo: CleaningsRepository = Depends(get_repository(CleaningsRepository))
) -> CleaningPublic:
    cleaning = await cleanings_repo.get_cleaning_by_id(id=id)

    if not cleaning:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail='No cleaning found with that id'
        )
    return cleaning
