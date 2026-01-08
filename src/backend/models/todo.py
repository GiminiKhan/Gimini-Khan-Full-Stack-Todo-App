from sqlalchemy import String, Boolean, UUID, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base, TimestampMixin
import uuid


class Todo(Base, TimestampMixin):
    __tablename__ = "todos"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=True)
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    priority: Mapped[int] = mapped_column(Integer, default=1, nullable=False)  # 1: low, 2: medium, 3: high, 4: urgent
    owner_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    project_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=True)

    # Relationships
    owner: Mapped["User"] = relationship("User", back_populates="todos")
    project: Mapped["Project"] = relationship("Project", back_populates="todos")

    def __repr__(self):
        return f"<Todo(id={self.id}, title='{self.title}', is_completed={self.is_completed}, owner_id={self.owner_id})>"