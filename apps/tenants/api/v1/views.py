from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from drf_spectacular.utils import extend_schema

from apps.core.renderers import IlimiAPIRenderer
from apps.tenants.models import School, Branch, SchoolMember

from .serializers import (
    SchoolSerializer,
    SchoolUpdateSerializer,
    BranchSerializer,
    BranchCreateSerializer,
    SchoolMemberSerializer,
    SchoolMemberInviteSerializer,
)


# ── Mixin ─────────────────────────────────────────────────────────────────

class SchoolScopedMixin:
    def get_school(self):
        member = SchoolMember.objects.filter(
            user=self.request.user, is_active=True
        ).select_related("school").first()
        if not member:
            raise NotFound("No school found for your account.")
        return member.school


# ── School ────────────────────────────────────────────────────────────────

@extend_schema(tags=["Schools"])
class SchoolMeView(SchoolScopedMixin, GenericAPIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [IlimiAPIRenderer]
    serializer_class = SchoolSerializer

    def get(self, request, *args, **kwargs):
        school = self.get_school()
        serializer = SchoolSerializer(school)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        school = self.get_school()
        serializer = SchoolUpdateSerializer(school, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "School details updated.",
                **SchoolSerializer(school).data,
            }
        )


# ── Branches ──────────────────────────────────────────────────────────────

@extend_schema(tags=["Schools"])
class BranchListCreateView(SchoolScopedMixin, GenericAPIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [IlimiAPIRenderer]
    serializer_class = BranchSerializer

    def get(self, request, *args, **kwargs):
        school = self.get_school()
        branches = Branch.objects.filter(school=school)
        serializer = BranchSerializer(branches, many=True)
        return Response({"branches": serializer.data, "count": branches.count()})

    def post(self, request, *args, **kwargs):
        school = self.get_school()
        serializer = BranchCreateSerializer(
            data=request.data, context={"school": school}
        )
        serializer.is_valid(raise_exception=True)
        branch = serializer.save(school=school)
        return Response(
            {
                "message": f"Branch '{branch.name}' created successfully.",
                **BranchSerializer(branch).data,
            },
            status=status.HTTP_201_CREATED,
        )


@extend_schema(tags=["Schools"])
class BranchDetailView(SchoolScopedMixin, GenericAPIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [IlimiAPIRenderer]
    serializer_class = BranchSerializer

    def get_branch(self, school, pk):
        try:
            return Branch.objects.get(school=school, pk=pk)
        except Branch.DoesNotExist:
            raise NotFound("Branch not found.")

    def get(self, request, pk, *args, **kwargs):
        school = self.get_school()
        branch = self.get_branch(school, pk)
        return Response(BranchSerializer(branch).data)

    def patch(self, request, pk, *args, **kwargs):
        school = self.get_school()
        branch = self.get_branch(school, pk)
        serializer = BranchCreateSerializer(
            branch,
            data=request.data,
            partial=True,
            context={"school": school},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "Branch updated successfully.",
                **BranchSerializer(branch).data,
            }
        )


# ── Members ───────────────────────────────────────────────────────────────

@extend_schema(tags=["Schools"])
class MemberListInviteView(SchoolScopedMixin, GenericAPIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [IlimiAPIRenderer]
    serializer_class = SchoolMemberSerializer

    def get(self, request, *args, **kwargs):
        school = self.get_school()
        members = SchoolMember.objects.filter(school=school).select_related(
            "user", "branch"
        )
        serializer = SchoolMemberSerializer(members, many=True)
        return Response({"members": serializer.data, "count": members.count()})

    def post(self, request, *args, **kwargs):
        school = self.get_school()
        serializer = SchoolMemberInviteSerializer(
            data=request.data, context={"school": school}
        )
        serializer.is_valid(raise_exception=True)

        # TODO: wire to invite service
        return Response(
            {"message": "Invitation sent successfully."},
            status=status.HTTP_201_CREATED,
        )