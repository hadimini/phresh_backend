from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException, Path
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

from app.api.dependencies.database import get_repository
from app.db.repositories.cleanings import CleaningsRepository
from app.models.cleaning import CleaningCreate, CleaningPublic, CleaningUpdate

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


@router.put('/{id}/', response_model=CleaningPublic, name='cleanings:update-cleaning-by-id')
async def update_cleaning_by_id(
        id: int = Path(..., ge=1, title='The id of the cleaning to be updated'),
        cleaning_update: CleaningUpdate = Body(..., embed=True),
        cleanings_repo: CleaningsRepository = Depends(get_repository(CleaningsRepository)),
) -> CleaningPublic:
    updated_cleaning = await cleanings_repo.update_cleaning(
        id=id,
        cleaning_update=cleaning_update
    )

    if not updated_cleaning:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail='No cleaning found with that id'
        )

    return updated_cleaning
