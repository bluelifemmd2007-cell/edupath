from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_URL = f"sqlite:///{BASE_DIR / 'edupath.db'}"
JWT_SECRET = "edupath-secret-change-in-production"
JWT_ALGORITHM = "HS256"
JWT_EXPIRE_DAYS = 7
