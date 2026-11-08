import { Suspense } from "react";
import Studio from "@/components/Studio";

export const metadata = { title: "Image studio · Frameforge" };

export default function ImagePage() {
  return (
    <Suspense>
      <Studio mode="image" />
    </Suspense>
  );
}
